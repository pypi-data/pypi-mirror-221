class Invite:
    def __init__(self, instance):
        self.instance = instance

    def create(self):
        pass

    def delete(self):
        pass

    def get(self):
        return [Participant(self.instance)]


class Participant:
    def __init__(self, instance):
        self.instance = instance
