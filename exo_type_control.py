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
    def wrapper(*args, **kw):
        locales = locals()
        annots = f.__annotations__
        positionals= getfullargspec(f)[0]
        # print(locales)
        # print(annots)
        # print(positionals)
        
        # # paramètres nommés à l'appel
        for param, value in locales["kw"].items():
            if param in annots and not isinstance(value, annots[param]):
                raise TypeError(f"{param}: {value} not a {annots[param].__name__} !")
        
        # paramètres positionnels
        for i, value in enumerate(locales["args"]):
            if positionals[i] in annots and not isinstance(value, annots[positionals[i]]):
                raise TypeError(f"{positionals[i]}: {value} not a {annots[positionals[i]].__name__} !")
        return f(*args, **kw)
    return wrapper

@type_control
def target(a: int, b, c: str = "default"):
    print(a, b, c)

# target(0, 3.14, "hello")
# target("hi", 3.14)
try:
    target(b=3.14, a=[], c="hello")
except TypeError as te:
    print(te)
# %%
