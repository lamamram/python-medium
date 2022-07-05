# %%
# soit une fonction disposant d'annotations sur des types simples
# int, str, list, tuple, dict, float

# écrire un décorateur qui va regarder si les paramètres sont bien 
# de l'instance décrite dans l'annotation si celle ci existe
# et lancer une exception TypeError si ce n'est pas le cas

# HINTS:
# func.__annotations__
# la fonction locals() qui renvoie le dictionnaire des variables locales
# le module inspect et la fonction getfullargspec
from inspect import getfullargspec

def type_control(f):
    def wrapper(*a, **kw):
        pass
        return f(*a, **kw)
    return wrapper

@type_control
def target(a: int, b, c: str = "default"):
    print(a, b, c)

target(0, 3.14, "hello")
target("hi", 3.14, "hello")
target(b=[], a=1)