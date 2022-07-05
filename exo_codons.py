# %%
# découper une chaine de caractère en triplets
from random import randint, shuffle

# fabrication d'une chaine d'adn random
sequence = "".join([ (3*randint(1, 10)) * char for char in "ATCG" ])
sequence = list(sequence)
shuffle(sequence)
sequence = "".join(sequence)
sequence

# transformer la chaine en liste de chaines de longueur 3


# %%
