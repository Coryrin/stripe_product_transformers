from observers.observable import Observable
from observers.product_observer import ProductObserver
import uuid

class Product(Observable):
    def __init__(self):
        super().__init__()
        self.id = None
        self.attach_observer(ProductObserver())
    
    def save(self, name: str, price: float):
        self.name = name
        self.price = price

        if self.id is None:
            self.id = uuid.uuid4()
            self.notify_observers('created', product=self)
            return
        
        self.notify_observers('updated', product=self)