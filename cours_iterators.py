# %%
# un itérable / itérateur est une classe qui 
# définit 3 méthodes magiques __init__, __iter__ et __next__ 

class Pow:
    # cond finale
    def __init__(self, exp, limit) -> None:
        self.limit = limit
        self.exp = exp

    # retourne un itérateur avec RAZ du compteur
    def __iter__(self):
        self.cpt = 0
        return self

    # test de la limite 
    # calcul de la valeur suivante
    # ou arrêt
    def __next__(self):
        if self.cpt < self.limit:
            ret = self.cpt**self.exp
            self.cpt += 1
            return ret
        else:
            raise StopIteration

p = Pow(2, 10)



# %%
# itération pas à pas
# obtentinon de l'itérateur à partir de l'itérable
it = iter(p)

for _ in range(11):
    print(next(it))
# %%
# for utiliser iter et next, et capture l'exception StopIteration
for i in p:
    print(i)
for i in p:
    print(i)
# %%
# fonctions usuelles sur les itérateurs / itérables
p = Pow(3, 5)

print(sum(p))
print(list(p))

first, second, third, *others = p
print(first, second, third, others[3:])
# %%
