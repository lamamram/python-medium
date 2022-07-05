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
