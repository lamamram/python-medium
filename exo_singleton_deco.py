# %%

from numpy import single


def single_deco(cls):
    # une fonction est un objet
    # on peut créer des attributs
    single_deco.instances = {}
    def wrapper(*a, **kw):
        if cls.__name__ not in single_deco.instances:
            single_deco.instances[cls.__name__] = cls()
        return single_deco.instances[cls.__name__]
    return wrapper

@single_deco
class Single: pass

@single_deco
class Single2: pass

s1, s11 = Single(), Single()
s2, s22 = Single2(), Single2()

s1 is s11, s2 is s22, s1 is s2
# %%
