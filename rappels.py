# %%
# rappels sur les types de paramètres

# ------positionnels, pos. optionnels, nommés -----, nommés optionnels
def proto(pos1, pos2, *args,          opt="default", **kwds):
    return pos1, pos2, args, opt, kwds

print(proto(1, 2, 3, 4, opt="hello", k1=5, k2=6))
# si nommé  + *args, commencer par *args
print(proto(1, 2, 3, 4))

# appels positionnels
# ou appels nommés
print(proto(pos2=2, opt="hi", pos1=1))

# unpacking d'une liste dans une fonciton => params positionnels
params = [1, 2, 3, 4, "hello"]
# proto(params[0], params[1],...)
print(proto(*params))

# unpacking d'un dico dans une fonciton => params nommés
keywords = {"opt": "hello", "pos2": 2, "pos1": 1, "k1": 5, "k2": 6}
print(proto(**keywords))

# ou les deux
keywords = {"opt": "hello", "k1": 5, "k2": 6}
print(proto(*params, **keywords))

# remise en ordre des appels depuis la depuis la définition
def proto_constraint(pos1, /, opt="dflt", *, mandatory="smthng"):
    return pos1, opt, mandatory

# "/" => paramètres à gauche appelables uniquement de façon positionnelle
# TypeError
# print(proto_constraint(pos1=1, opt=2, mandatory=3))

# "*" => paramètres à droite appelables uniquement de façon nommés
# TypeError
# print(proto_constraint(1, 2, 3))

# %%
print("another cell")
# %%
# docstring & indications de types

def proto(measure: float, objs: list, msg: str) -> tuple:
    """
    fonction qui utilise les type hinting 
    """
    return measure, objs, msg

# surtout documentaire
print(proto("blabla", {}, 1))

# accès à la doc et les annotations
print(proto.__doc__)
print(proto.__annotations__)

# %%
# "man" python
help(proto)
# %%
# connaitre les attributs d'un objet
dir(proto)

# %%
# passage par réference

x = 1
y = x

# adresses de x et y: y référence la variable x
print(id(x), id(y), x is y)

# réaffactation => changement de case
y = x + 2
print(id(x), id(y), x is y)
# %%
# python optimise la gestion des litéraux de type int float, str
x, y = 1, 1
x is y
# %%
# avertissement 1: pour les mutables (list, dict, customs...)

l1 = [1, 2, 3]
l2 = l1
# copie disjointe en mémoire => copie creuse
l3 = l1.copy()
l4 = l1[:]

l2.append(4)
print(l1)

l1 is l3, l1 is l4


# %%
# avertissment 2 : pourles fonctions avec les mutables
def func(lst: list, v):
    print(f"param: {id(lst)}")
    lst.append(v)


l = [1, 2, 3]
print(f"l: {id(l)}")
func(l, 4)
print(l)
# %%
# portée des variables en python
# une variable est utilisable dans son scope et
# les fonctions définies dedans
def func():
    print(x + 1)

x = 1

func()

# %%
def func():
    x = 2
    print(f"x local: {id(x)}")
    print(locals())

x = 1
print(f"x global: {id(x)}")

func()
print(globals())
# %%
# modification d'une globale dans une fonction
def func():
    global x
    print(f"x global: {id(x)}")
    x += 1
    print(locals())

x = 1
print(f"x global: {id(x)}")
func()
print(f"valeur de x post fonction: {x}")

# %%
# unpacking

x, y = 0, 1

def func():
    return 0, 1

x, y = func()
z = func()
z[0], z[1], x, y
# %%
# expression vs instruction
# expression : => evaluable: variable, literal, calcul
x = 0
# instruction: ligne de code avec des mots clés
# print(x=1)
# print(return 0)
# %%
# opérateur ternaire en python
cond = True
if cond:
    value = "val"
else:
    value = "default"

value = "val" if cond else "default"

# %% liste en intension: objet qui contient sa définition
fruits = ["pomme", "poire", "banane"]

[ fruit.upper() for fruit in fruits if fruit[0] == "p" ]
{fruit: fruit.upper() for fruit in fruits}

# %%
# itérations sur dico
for k in {"k1": "v1", "k2": "v2"}:
    print(k)

for v in {"k1": "v1", "k2": "v2"}.values():
    print(v)

for k, v in {"k1": "v1", "k2": "v2"}.items():
    print(k, v)

tuples = list({"k1": "v1", "k2": "v2"}.items())
d = dict(tuples)

keys, values = d.keys(), d.values()
dict(zip(keys, values))
# %%

class C:
    pass

c = C()
dir(c)
setattr(c, "param", "value")
setattr(c, "func", lambda x: x+2)
getattr(c, "param")
getattr(c, "func")(2)

# %%
# propriétés
class C:
    _name = ""
    name=property(lambda self: getattr(self, '_name'),
lambda self, value: setattr(self, '_name', value))

c = C()
c.name = "v"
print(c.name)
        
# %%
class C:
    def __init__(self, t) -> None:
        self.truc = t

    def __str__(self) -> str:
        return f"obj: truc = {self.truc}"
    
    def __del__(self):
        print("deletion ! ")

c = C("TRUC")
print(c)
del c

# %%
# else pour for et while
# le bloc else s'exécute si la boucle 
# se termine normalement
# for => itérable entièrement consommé
# while => on sort sur la condition de la boucle

# le bloc else ne s'exécute pas si la boucle 
# casse sur un break

break_value = 11
for i in range(10):
    if i == break_value: break
else:
    print(f"{i} == 9 !")

i = 10
while i > 0:
    i -= 1
    break
else:
     print(f"{i} == 0 !")



# %%
# les fichiers sont des itérateurs
f = open("cours_lambdas.py", "r")
print(next(f))
f.close()

# %%
# gestionaire de contexte: with
# la resource est refermée en sortant du bloc
with open("cours_lambdas.py", "r") as f:
    print(next(f))

# %%
# all et any
l = [1, 0, 3, 4]
# all vrai si tout est vrai
all(l)
# any est vrai si ou moins un élément est vrai
any(l)
# %%

try:
    # 3/0
    3
    quit(0)
except ZeroDivisionError as ze:
    print(ze)
else:
    print("no exception")
finally:
    print("whatever it takes")



# %%
