import os
from itertools import combinations
from multiprocessing import Pool, cpu_count, current_process
# pip install geopy
from geopy.distance import geodesic
import csv
from zipfile import ZipFile

# exo:
# 1/ ouvrir le fichier villes_frances.csv (avec csv ou pandas)
# répartir les lignes dans un dictionnaire dont les clés
# sont les départements
# {
#     "01": [{"name": '', "lat": '', "lon": ''}]
# }

# 2/ lancer un pool de process sur un worker qui calcule
# la distance max entre deux villes d'un même dept (tester
# avec 4, 5 depts)

# 3/ rassembler les résultats pout trouver le max global

def worker(task):
    return f"{task} done by {current_process().name}"


if __name__ == "__main__":
    with Pool(processes=cpu_count() - 2) as pool:
        # appels unique synchrone
        # multiples araguments
        unique_call = pool.apply(worker, args=("task 1",))
        # appels répartis sur plusieurs processes
        # un seul argument par worker
        five_calls = pool.map(worker, [f"taks {i}" for i in range(2,7)])
        # plusieurs arguments
        # pool.starmap(worker, [(arg1, arg2), (arg11, arg22)....])
        # fonctions async
        # apply_async, map_async, starmap_async
        # plus aucun lancement
        pool.close()
        pool.join()
        # appels asynchrones
        # apply_async.get(), map_async.get(), starmap_async.get()