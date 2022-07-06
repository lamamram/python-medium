# %%
# type d'une donnée
a = 1

type(a)
# type d'une classe: type
type(int)
# %%
class A:
    param=0
    def get_param(self): return self.param

a = A()
a.get_param()

# %%
# équivalent à
A = type("A", (), {"param": 0, "get_param": lambda self: self.param })
a = A()
a.get_param()
print(a.__class__.__name__)

# %%
# type est une métaclasse qui instancie des classes
# on peut créer sa propre metaclass en héritant de type
from typing import Any


# Truc() -> Meta.__new__ -> type.__new__
# -> Meta.__call__ -> Truc.__init__

# Meta.__new__ peut renvoyer une instance de classe
# qui sera transférée à l'objet Truc
# Meta.__call__ ne renvoie qu'une instance d'objet
class Meta(type):
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print("call meta")
        instance = super().__call__(*args, **kwds)
        instance.special2 = 10
        return instance

    def __new__(cls, name, bases, attrs):
        print("new class")
        instance = super().__new__(cls, name, bases, attrs)
        instance.special = 5
        return instance


class Truc(metaclass=Meta):
    def __init__(self) -> None:
        print("init obj")

t = Truc()

print(Truc.special)
print(t.special)
print(t.special2)
# %%
