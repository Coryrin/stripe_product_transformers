import stripe

class StripeService:
    def __init__(self, item_factory):
        self.stripe = stripe
        self.stripe.api_key = ''
        self.item_factory = item_factory

    def create_product(self, product):
        transformed_product = self.item_factory.get_transformer_for(product).transform(product)

        product = self.stripe.Product.create(
            name=transformed_product['name'],
            default_price_data=transformed_product['default_price_data']
        )