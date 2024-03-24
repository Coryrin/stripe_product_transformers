from services.stripe_service import StripeService

class ProductObserver:
    def event(self, event, **kwargs):
        if event == 'created':
            return self.created(kwargs['product'])
        elif event == 'updated':
            return self.updated(kwargs['product'])
        
    def created(self, product):
        stripe = StripeService()
        stripe.create_product(product)

    def updated(self, product):
        print('product updated')