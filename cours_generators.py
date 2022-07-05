# %%
# générateur simple
# simple_gen est la fonction génératrice
def simple_gen():
    yield 0
    yield "coucou"
    yield
    yield 3.14

# le générateur est l'objet obtenu par appel
# à la fonction génératrice
g = simple_gen()
g

# %%
# utilisation du générateur

for _ in range(4):
    print(next(g))

# recharger le générateur pour réitéter
# g = simple_gen()
for elem in simple_gen():
    print(elem)
# %%
# générateur de puissances
from sys import getsizeof

def pow(exp, limit):
    for i in range(limit):
        yield i**exp

p = pow(3, 1000)
instension = list(p)

print(getsizeof(p), getsizeof(instension))
# %%
# générateurs infinis (count, cycle, repeat ...)
def my_count(start=0):
    while True:
        yield start
        start += 1

mc = my_count(1)

# %%
# les ranges sont des générateurs
from sys import getsizeof

def my_range(stop, start=0, step=1):
    comp_operator = "<" if step >= 0 else ">"
    while eval(f"start {comp_operator} stop"):
        yield start
        start += step


print(getsizeof(my_range(10000000)))
getsizeof(range(100000000))

# %%
# imbrication des générateurs
# yield from itère complétement un générateur
def my_cycle(g_func, times=2):
    for t in range(times):
        yield from g_func()

def abcd():
    for l in 'abcd':
        yield l

for elem in my_cycle(abcd):
    print(elem)

# %%
# exemple send
def double(val=2):
    while True:
        val *= 2
        # 1. une instruction yield est une expression != return
        # par défaut cette expression vaut None
        # generator.send fourni une valeur à cette expression
        val = yield val

d = double()
print(next(d))
# send consomme une itération comme next
print(d.send(3))
print(d.send(6))
# %%
