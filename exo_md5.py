# %%
from hashlib import md5
from string import ascii_lowercase

h = md5(bytes("coucou", encoding="utf8"))
print(h.hexdigest())

target= "3ed7dceaf266cafef032b9d5db224717"

# trouver la chaine en clair
# HINT: faire une attaque brute force
# => toute les chaines possibles
# à partir des lettre minuscules et pas d'espace



