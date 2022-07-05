# %%
from hashlib import md5
from itertools import product, count
from string import ascii_lowercase

# h = md5(bytes("coucou", encoding="utf8"))
# print(h.hexdigest())

target= "3ed7dceaf266cafef032b9d5db224717"

# trouver la chaine en clair
# HINT: faire une attaque brute force
# => toute les chaines possibles
# à partir des lettre minuscules et pas d'espace
for i in count(1):
    for p in product(ascii_lowercase, repeat=i):
        s = "".join(p)
        if md5(bytes(s, encoding="utf8")).hexdigest() == target:
            print(s)
            break
    else: continue
    break



# %%

print(list(product("abcd", repeat=3)))


# %%
