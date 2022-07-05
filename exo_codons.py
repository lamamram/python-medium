# %%
# découper une chaine de caractère en triplets
from random import randint, shuffle
from itertools import islice

# fabrication d'une chaine d'adn random
sequence = "".join([ (3*randint(1, 4)) * char for char in "ATCG" ])
sequence = list(sequence)
shuffle(sequence)
sequence = "".join(sequence)
sequence

# %%
# transformer la chaine en liste de chaines de longueur 3
l = len(sequence)
slices = [ islice(sequence, i, l, 3) for i in range(3) ]
tuples = list(zip(*slices))
list(map(lambda t: "".join(t) , tuples))

# %%
[ sequence[i:i+3] for i in range(0, l, 3) ]
# %%
