# %%
class SingleMeta(type):
    __instance = None

    def __call__(cls, *args, **kwds):
        if not cls.__instance:
            instance = super().__call__(*args, **kwds)
            cls.__instance = instance
        return cls.__instance

class Single(metaclass=SingleMeta):
    pass

class Single2(metaclass=SingleMeta):
    pass

s1, s11 = Single(), Single()
s2, s22 = Single2(), Single2()

s1 is s11, s2 is s22, s1 is s2
# %%
