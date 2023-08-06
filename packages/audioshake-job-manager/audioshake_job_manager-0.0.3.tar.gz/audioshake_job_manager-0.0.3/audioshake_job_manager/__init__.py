from concurrent.futures import Future
import json
import logging
import os
import abc

import boto3

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", None)

JOB_TIMEOUT = int(os.environ.get("JOB_TIMEOUT", "60"))

logger = logging.getLogger(__name__)


class JobManager:
    __metaclass__ = abc.ABCMeta

    def __init__(self, queue_url: str, max_number_of_message: int = 10, batch: int = 1):
        self.max_number_of_message = max_number_of_message
        self.queue_url = queue_url
        # NOTE to be used for batching messages read from the queue.
        self.batch = batch

        self.sqs_client = boto3.client(
            "sqs", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL
        )
        self.step_function_client = boto3.client(
            "stepfunctions", region_name=AWS_REGION, endpoint_url=AWS_ENDPOINT_URL
        )

    def __reduce__(self):
        return (self.__class__, ())

    def start(self):
        logging.basicConfig(level=logging.INFO)

        logger.info(f"Starting job processor")
        logger.info(f"Listening on queue: {self.queue_url}")

        try:
            while True:
                self._process_jobs()
        except Exception:
            logger.error(f"Error processing jobs", exc_info=True)

    def _process_jobs(self):
        response = self.sqs_client.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=self.max_number_of_message,
            WaitTimeSeconds=1,
            AttributeNames=["All"],
        )

        jobs = response.get("Messages", [])
        if not jobs:
            return

        futures: list[Future] = []
        cache: dict = {}
        for job in jobs:
            logger.info("submitting request: %s", job)
            body = json.loads(job["Body"])
            task_token = body.pop("task_token")

            payload = body["input"]
            logger.info("sending payload: %s", payload)

            future = self.process(json.dumps(payload))
            futures.append(future)
            cache[future._id] = {
                "job_id": job["ReceiptHandle"],
                "task_token": task_token,
            }

        self._process_results(futures, cache)

    def _process_results(self, futures: list[Future], cache: dict = {}):
        for future in futures:
            try:
                result = future.result(timeout=JOB_TIMEOUT)
                # TODO: process batch results.
                response = result[0] if isinstance(result, list) else result
                logger.info("response: %s", response)
            except TimeoutError as exc:
                error_message = "Future timed out"
                response = {"success": False, "error": error_message}
                logger.exception(error_message)
            except Exception as exc:
                error_message = f"Unknown error occured. {exc}"
                response = {"success": False, "error": error_message}
                logger.exception(error_message)
            finally:
                self.sqs_client.delete_message(
                    QueueUrl=self.queue_url, ReceiptHandle=cache[future._id]["job_id"]
                )
                self.step_function_client.send_task_success(
                    taskToken=cache[future._id]["task_token"],
                    output=json.dumps(response),
                )

    @abc.abstractmethod
    def process(self, payload: str) -> Future:
        raise NotImplementedError("")

    @abc.abstractmethod
    def process_batch(self, payload: list[str]) -> list[Future]:
        raise NotImplementedError("")
