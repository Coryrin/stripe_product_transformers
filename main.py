from models.product import Product

product_one = Product()
# This one hits created
product_one.save('PS5', 400.00)
# This one hits updated
product_one.save('PS5', 500.00)



