# %%
# compteur d'occurences de mots dans un texte
import re
from string import punctuation
from itertools import groupby

text = """
Python (prononcé /pi.tɔ̃/) est un langage de programmation interprété, multi-paradigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet. Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions ; il est ainsi similaire à Perl, Ruby, Scheme, Smalltalk et Tcl.

Le langage Python est placé sous une licence libre proche de la licence BSD4 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux5, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser.

Il est également apprécié par certains pédagogues qui y trouvent un langage où la syntaxe, clairement séparée des mécanismes de bas niveau, permet une initiation aisée aux concepts de base de la programmation6.
"""
# virer la ponctuation, les \n etc..
text = re.sub(f"[{punctuation}]", " ", text)
text = re.sub("\\r?\\n", " ", text)
text = re.sub(" +", " ", text)
words = text.lower().split()
words = list(filter(lambda w: len(w) > 3, words))

# trier
words.sort()

# regrouper 
occurences = map(
    lambda gb: (gb[0], len(list(gb[1]))),
    groupby(words)
)
# trier les occurences
occurences = sorted(
    occurences,
    key=lambda t: t[1],
    reverse=True
)
dict(occurences)
# %%
