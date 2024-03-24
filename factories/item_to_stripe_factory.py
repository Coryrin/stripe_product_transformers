class ItemToStripeFactory:
    def __init__(self, transformers):
        self.transformers = transformers

    def get_transformer_for(self, cls):
        for transformer in self.transformers:
            if transformer.handles(cls):
                return transformer
        
        raise ValueError(f'Unknown transformer for class {cls.__class__.__name__}')