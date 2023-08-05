# Standard Library
import logging

# Project Library
from elsdk.events import Events

logger = logging.getLogger(__name__)


class ELSDK:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.events = Events(self)
        logger.info("Initializing the Einston Labs SDK")

    def __get_token(self):
        pass

    def __validate_token(self):
        pass
