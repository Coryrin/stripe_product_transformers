class PlanToStripeProductDTO:
    def handles(self, cls) -> bool:
        # return isinstance(cls, Plan)
        return cls.__class__.__name == 'Plan'
    
    def transform(self, plan):
        return {
            "name": plan.name,
            "default_price_data": {
                "currency": "GBP",
                "unit_amount": int(plan.fee * 100),
                "recurring": plan.recurring,
            }
        }