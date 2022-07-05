# %%
from functools import wraps
# décorateur: fonction qui prend une fonction
# en paramètre et retourne une autre fonction
# qui est définie à l'intérieur

def deco(f):
    # décorateur de transfert de la doc et du nom 
    # de f sur wrapper
    @wraps(f)
    def wrapper(*args, **kwds):
        print("traitments avant")
        ret = f(*args, **kwds)
        print("traitements après")
        return ret
    return wrapper


@deco
def to_upper(s):
    """
    super foncition passe en MAJ
    """
    return s.upper()

# strictement équivalent à
# to_upper = deco(to_upper)

to_upper("bonjour")


# %%
# décorateur functools.wraps pour retrouver la doc
# de la fonction initiale
help(to_upper)


# %%
# décorateurs multiples

def strong(f):
    def wrapper(*a, **kw):
        return f"<strong>{f(*a, **kw)}</strong>"
    return wrapper

def italic(f):
    def wrapper(*a, **kw):
        return f"<em>{f(*a, **kw)}</em>"
    return wrapper

@italic
@strong
def to_upper(s):
    """
    super fonction passe en MAJ
    """
    return s.upper()

# équivalent à
# to_upper = italic(strong(to_upper))

to_upper("hello")

# %%
# décorateur paramétré

def tag(*tags):
    def deco(f):
        def wrapper(*a, **kw):
            ret = f(*a, **kw)
            for t in tags:
                ret = f"<{t}>{ret}</{t}>"
            return ret
        return wrapper
    return deco

@tag("strong", "em")
def to_upper(s):
    """
    super fonction passe en MAJ
    """
    return s.upper()

to_upper("hello")

# %%

class Truc:
    # attributs de classe
    __nb_occurences = 0

    def __init__(self, param):
        self.param = param
        # attribut d'objet
        self.__nb_occurences += 1
    
    # méthode d'objet
    # le premier paramètre est l"instance
    def get_occurences(self):
        return self.__nb_occurences
    
    @classmethod
    def add_occurences(cls):
        cls.__nb_occurences += 1
    
    # méthode de classe
    # appelable autant sur l'objet que sur la classe
    # le premier paramètre est l'objet de classe
    @classmethod
    def class_occurences(cls):
        return cls.__nb_occurences

    # méthode statique
    # méthode de classe sans accès à cls
    @staticmethod
    def static():
        return 'hello'

t = Truc("bla")
Truc.add_occurences()
t2 = Truc("blo")
Truc.add_occurences()
t3 = Truc("bli")
# contournement d'un attribut privé
# t._Truc__nb_occurences
# Truc._Truc__nb_occurences

print(t.get_occurences())
# t2 instancié avec param de classe à 1
print(t2.get_occurences())
# t3 instancié avec param de classe à 2
print(t3.get_occurences())

Truc.class_occurences()

Truc.static()
# %%
