from models.plan import Plan

class PlanToStripeProductDTO:
    def handles(self, cls) -> bool:
        return isinstance(cls, Plan)
    
    def transform(self, plan):
        return {
            "name": plan.name,
            "default_price_data": {
                "currency": "GBP",
                "unit_amount": plan.fee * 100,
                "recurring": plan.recurring,
            }
        }