from models.product import Product
from models.plan import Plan
from factories.item_to_stripe_factory import ItemToStripeFactory
from dto.product_to_stripe import ProductToStripeProductDTO
from dto.plan_to_stripe import PlanToStripeProductDTO

if __name__ == '__main__':
    fac = ItemToStripeFactory([
        ProductToStripeProductDTO(),
        PlanToStripeProductDTO(),
    ])
    product_one = Product()
    # This one hits created
    product_one.save('PS5', 400.00)
    # This one hits updated
    product_one.save('PS5', 500.00)

    plan_one = Plan()
    plan_one.name = 'Gold Monthly'
    plan_one.fee = 10
    plan_one.recurring = 'monthly'

    transformed = fac.get_transformer_for(product_one).transform(product_one)
    transformed_plan = fac.get_transformer_for(plan_one).transform(plan_one)
    print(transformed_plan)
