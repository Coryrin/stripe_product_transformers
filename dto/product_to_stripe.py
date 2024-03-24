from models.product import Product

class ProductToStripeProductDTO:
    def handles(self, cls) -> bool:
        return isinstance(cls, Product)
    
    def transform(self, product):
        return {
            "name": product.name,
            "default_price_data": {
                "currency": "GBP",
                "unit_amount": product.price * 100 
            }
        }