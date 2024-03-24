import uuid
from observers.observable import Observable

class Plan(Observable):
    def __init__(self):
        super().__init__()
        self.id = None

    def save(self, name, fee, recurring):
        self.name = name
        self.fee = fee
        self.recurring = recurring

        if self.id is None:
            self.id = uuid.uuid4()
            return
