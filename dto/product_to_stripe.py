from models.product import Product

class ProductToStripeProductDTO:
    def handles(self, cls) -> bool:
        return isinstance(Product, cls)
    
    def transform(self, product):
        return {
            "name": product.name,
            "default_price_data": {
                "currency": "GBP",
                "unit_amount": 1000 
            }
        }