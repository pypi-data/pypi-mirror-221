# Project Library
from elsdk.invite import Invite
from elsdk.utils.exceptions import InCompatibleTypeException


class Session:
    def __init__(self, instance):
        self.instance = instance

    def create(self, participant_id):
        if not isinstance(Invite, participant_id):
            raise InCompatibleTypeException("Expecting Participant Object")
