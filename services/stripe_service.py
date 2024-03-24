import stripe
from factories.item_to_stripe_factory import ItemToStripeFactory
from dto.product_to_stripe import ProductToStripeProductDTO
from dto.plan_to_stripe import PlanToStripeProductDTO

class StripeService:
    def __init__(self):
        self.stripe = stripe
        self.stripe.api_key = ''

    def create_product(self, product):
        fac = ItemToStripeFactory([
            ProductToStripeProductDTO(),
            PlanToStripeProductDTO(),
        ])

        transformed_product = fac.get_transformer_for(product).transform(product)

        product = self.stripe.Product.create(
            name=transformed_product['name'],
            default_price_data=transformed_product['default_price_data']
        )