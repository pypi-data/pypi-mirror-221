# Project Library
from elsdk.infra import Infra
from elsdk.invite import Invite
from elsdk.session import Session
from elsdk.state import State


class Events:
    def __init__(self, instance):
        self.instance = instance

    def create(self):
        return EventDetail(self.instance)

    def delete(self):
        pass

    def get(self):
        return [EventDetail(self.instance), EventDetail(self.instance)]


class EventDetail:
    def __init__(self, instance):
        self.instance = instance
        self.participants = Invite(self)
        self.session = Session(self)
        self.infra = Infra(self)
        self.state = State(self)

    def schedule(self):
        pass

    def update(self):
        pass
