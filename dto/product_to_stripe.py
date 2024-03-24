class ProductToStripeProductDTO:
    def handles(self, cls) -> bool:
        # return isinstance(cls, Product)
        return cls.__class__.__name__ == 'Product'
    
    def transform(self, product):
        return {
            "name": product.name,
            "default_price_data": {
                "currency": "GBP",
                "unit_amount": int(product.price * 100)
            }
        }