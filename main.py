from models.product import Product
from models.plan import Plan

if __name__ == '__main__':
    product_one = Product()
    # This one hits created
    product_one.save('PS5', 400.00)
    # This one hits updated
    product_one.save('PS5', 500.00)

    plan_one = Plan()
    plan_one.name = 'Gold Monthly'
    plan_one.fee = 10
    plan_one.recurring = 'monthly'
