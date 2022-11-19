from aiologger import Logger

from service.exceptions.common import CommonException
from service.utils.formatter import format_error, trim_extra_whitespaces


class Log:
    logger: Logger

    @classmethod
    async def initialise_logger(cls):
        cls.logger = Logger.with_default_handlers()

    @classmethod
    async def shutdown_logger(cls):
        await cls.logger.shutdown()

    @classmethod
    async def log_debug(cls, message: str):
        output = f"[DEBUG]\t" f"MESSAGE: {message}"
        await cls.logger.debug(output)

    @classmethod
    async def log_exception(cls, error: CommonException):
        formatted_error = format_error(error.error)
        output = (
            f"[EXCEPTION]\t"
            f"TYPE: {error.__class__.__name__}, "
            f"MESSAGE: {error.message}, "
            f"TRACEBACK:\n{formatted_error}"
        )
        await cls.logger.exception(output)

    @classmethod
    async def log_request_start(cls, method: str, path: str, time: str, ip: str):
        output = (
            f"[INFO]\t"
            f"STATUS: started, "
            f"METHOD: {method}, "
            f"PATH: {path}, "
            f"TIME: {time}, "
            f"IP: {ip}"
        )
        await cls.logger.info(output)

    @classmethod
    async def log_request_end(
        cls, method: str, path: str, time: str, delta: str, ip: str
    ):
        output = (
            f"[INFO]\t"
            f"STATUS: ended, "
            f"METHOD: {method}, "
            f"PATH: {path}, "
            f"TIME: {time}, "
            f"DELTA: {delta}, "
            f"IP: {ip}"
        )
        await cls.logger.info(output)
