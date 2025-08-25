class FromDictMixin:
    @classmethod
    def from_dict(cls, d):
        d = {k: v for k, v in d.items() if k in cls.__annotations__}
        return cls(**d)