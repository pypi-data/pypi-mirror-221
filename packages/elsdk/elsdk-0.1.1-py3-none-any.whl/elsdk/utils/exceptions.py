# Standard Library
import logging

logger = logging.getLogger(__name__)


class ELSDKException(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "ELSDK Exception"
        logger.exception(logger)
        super().__init__(msg)


class InCompatibleTypeException(ELSDKException):
    """
    Incompatible data provided
    """

    pass


class NetworkException(ELSDKException):
    """
    Exception raised when network connectivity issues arised
    """

    pass


class PlatformNotSupportedException(ELSDKException):
    pass


class OperationNotFound(ELSDKException):
    pass
