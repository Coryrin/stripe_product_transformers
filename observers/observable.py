class Observable:
    def __init__(self):
        self.observers = []

    def attach_observer(self, cls):
        self.observers.append(cls)
    
    def notify_observers(self, event, **kwargs):
        for observer in self.observers:
            observer.event(event, **kwargs)