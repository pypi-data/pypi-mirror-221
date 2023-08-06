"""
    QuaO Project device.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from abc import abstractmethod, ABC

from ...data.job.job_response import JobResponse
from ...enum.job_status import JobStatus
from ...enum.media_type import MediaType
from ...model.provider.provider import Provider
from ...config.logging_config import *
from ...util.json_parser_util import JsonParserUtils


class Device(ABC):
    def __init__(self, provider: Provider, device_specification: str):
        self.provider = provider
        self.device = provider.get_backend(device_specification)
        self.execution_time = None

    def run_circuit(self, circuit, shots: int, post_processing) -> JobResponse:
        """

        @param post_processing:
        @param circuit:
        @param shots:
        """

        provider_job_id = ''
        content_type = None
        job_histogram = None

        try:
            job = self._create_job(circuit=circuit, shots=shots)
            provider_job_id = self._get_provider_job_id(job)
            job_status = self._get_job_status(job)
            job_result_dictionary = {}

            if self._is_simulator() or JobStatus.DONE.value.__eq__(job_status):
                job_result = job.result()
                job_result_post_processing = post_processing(job_result)

                job_status = self._get_job_status(job)

                logger.debug('Parsing job result....')
                job_result_dictionary = JsonParserUtils.parse(job_result_post_processing)
                logger.debug('Parsing job result completed!')

                content_type = MediaType.APPLICATION_JSON.value

                logger.debug('Producing histogram ....')
                job_histogram = self._produce_histogram_data(job_result)
                logger.debug('Producing histogram completed!')

                logger.debug('Calculating execution time ....')
                self._calculate_execution_time(job_result_dictionary)
                logger.debug('Execution time calculation was completed!')

        except Exception as exception:
            logger.debug('Exception when invoke job on device {0}: {1}'
                         .format(self._get_name(), str(exception)))

            job_result_dictionary = {
                "error": "Exception when invoke job on device: " + self._get_name(),
                "exception": str(exception)
            }

            job_status = JobStatus.ERROR.value

        return JobResponse(
            provider_job_id=provider_job_id,
            job_status=job_status,
            job_result=job_result_dictionary,
            content_type=content_type,
            job_histogram=job_histogram,
            execution_time=self.execution_time
        )

    @abstractmethod
    def _create_job(self, circuit, shots):
        """

        @param circuit:
        @param shots:
        """
        pass

    @abstractmethod
    def _is_simulator(self) -> bool:
        """

        """
        pass

    @abstractmethod
    def _produce_histogram_data(self, job_result) -> dict:
        """

        @param job_result:
        """
        pass

    @abstractmethod
    def _get_provider_job_id(self, job) -> str:
        """

        """
        pass

    @abstractmethod
    def _get_job_status(self, job) -> str:
        """

        """
        pass

    # @abstractmethod
    # def _parse_job_result(self, job_result) -> dict:
    #     """
    #
    #     """
    #     pass

    @abstractmethod
    def _get_name(self) -> str:
        """

        """
        pass

    @abstractmethod
    def _calculate_execution_time(self, job_result) -> float:
        """

        """
        pass
