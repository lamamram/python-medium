# %%
import csv
# générateur d'écriture dans le csv 
# sur commande
def gen_writer(filename, delimiter=","):
    with open(filename, "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f, delimiter=delimiter)
        while True:
            try:
                row = yield
                if all(map(lambda r: isinstance(r, list), row)):
                    writer.writerows(row)
                else:
                    print(row)
                    writer.writerow(row)
            except ValueError:
                break
            except GeneratorExit:
                return
    # en cas de throw, pour l'itératin suppl.
    # le fichier doit être fermé avant la fin du générateur
    yield


gw = gen_writer("test.csv", ";")
# commencer par une itération à vide
gw.send(None)
# next(gw)
gw.send(["id", "name", "age"])
# # ....
gw.send([[1, "bob", 34], [2, "jane", 22]])
gw.throw(ValueError)
 
# gw.close()
# %%
