# %%
import numpy as np
import pandas as pd

# %%
# définition d'une lambdas vs fonction nonmmée
from dis import dis

# annotation utiles pour l'autocompletion de l'éditeur
def func(param: str):
    param = list(param)
    # i  = 0
    for i, letter in enumerate(param):
        if letter not in "aeiouy":
            param[i] = letter.upper()
    #    i += 1
    return "".join(param)

print(func)
dis(func)

print(func("hello"))
# %%
# fonction éphémère, à usage unique
# pas de nom
# lambda --signature classique-- : --- 1 expression ----
func = lambda p: p.upper()
print(func)
dis(func)


# %%
# utilisation des lambdas
# 1. map à un itérable: application d'une transformation
# à tous les éléments d'un vecteur
chaines = ["str1", "str2", "str3"]
list(map(lambda p: p.upper(), chaines))

values = ["str1", 22, "str3"]
list(map(lambda p: p.upper() if isinstance(p, str) else -p, values))
# %%
# exo: map à 2 éléments
arr1, arr2 = [ np.random.randint(0, 10, size=10) for _ in range(2) ]
print(arr1, arr2)

# éléments de même valeur dans 2 itérables

sames = list(map(lambda e1, e2: e1 == e2, arr1, arr2))
# détecte les indices vrais
print(np.where(sames))
np.where(arr1 == arr2)


# %%
# map à n éléments
list(map(lambda *en: sum(en)/len(en), [1, 2, 4], [2,0,5], [2, 4]))

# %%
# iify: immediately invoked function
(lambda x: x**2)(5)

# %%
# filter
list(filter(lambda x: not x%2, range(0, 20)))

# %%
# reduce
from functools import reduce

# opération de proche en proche en accumulant les résultats intérmédiaires
# l'opération doit être transitive
reduce(lambda x, y: (x**2 + y**2)**0.5, [3, 6, 8, 4, 0, -6])/6

# %%
# tri complexes
rows = [f"row_{i}" for i in np.random.randint(0, 20, size=10)]
rows
sorted(rows)
rows.sort()
# on trie sur la valeur de retour de la fonction de tri
sorted(rows, key=lambda r: int(r[r.index("_") + 1:]), reverse=True)

# %%

# poids taille , tens sys, tens dia
patient0 = np.array([64.4, 173.8, 130, 80])
patient1 = np.array([52.4, 163.8, 146, 90])
patients = np.array([patient0, patient1])

patients.mean()
# moyennes des lignes
patients.mean(axis=0)
print((patient0 + patient1)/2)

# moyenne des colonnes
print([patient0.mean() , patient1.mean()])
patients.mean(axis=1).reshape(2, 1)

# rapport taille sur poids
np.apply_along_axis(lambda c: c[1]/c[0], axis=1, arr=patients)
# %%
# students = np.array([ [f"student_{i}"] * 4 for i in range(1, 11) ])
# students = np.concatenate(students)
# répétition de chaque élément de la liste 4 fois

student = [ f"student_{i}" for i in range(1, 11)]
subject = ["math", "english", "biology", "history"]

students = np.repeat(student, 4)
subjects = subject * 10
# répétition de la liste 4 fois
# students = np.tile(student, 4)

# notes entre 0 et 20 arrondies à 0.5
notes = np.random.randint(0, 20, size=40)
# clip assure que les résultats reste entre deux valeurs extrêmes
# ici 0 et 20
notes = np.clip(notes + 0.5*np.random.choice([0, 1], size=40), 0, 20)

notes_df = pd.DataFrame({
    "students": students,
    "subjects": subjects,
    "coeffs": np.tile([3, 3, 2, 2], 10),
    "notes": notes
})
notes_df

pivoted_df = notes_df.pivot(
    columns="subjects",
    values=["notes", "coeffs"],
    index="students"
)
pivoted_df


pivoted_df.apply(
    lambda row: np.average(row["notes"], weights=row["coeffs"]),
    axis=1
)

# %%
