class ProductObserver:
    def event(self, event, **kwargs):
        if event == 'created':
            return self.created(kwargs['product'])
        elif event == 'updated':
            return self.updated(kwargs['product'])
        
    def created(self, product):
        print('Product saved!')

    def updated(self, product):
        print('product updated')