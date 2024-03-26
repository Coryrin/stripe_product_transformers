from services.stripe_service import StripeService
from factories.item_to_stripe_factory import ItemToStripeFactory
from dto.product_to_stripe import ProductToStripeProductDTO
from dto.plan_to_stripe import PlanToStripeProductDTO

class StripeProductable:
    def __init__(self, item_factory):
        