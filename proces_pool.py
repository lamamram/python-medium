# %%
import csv, os
from itertools import combinations
from multiprocessing import Pool, current_process, cpu_count
from geopy.distance import geodesic
from zipfile import ZipFile

# Exo:
# 1) Ouvrir le fichier villefrance.csd (avec csv ou panda)
#    et Répartir les lignes dans un dictionnaire dont les clés sont les départements
# {
#  "01": [{"name": "", "lat": "", "lon":""}],
#  ...
# }
# 2) Lancer un pool de process sur un worker qui calcule la distance max entre deux villes d'un même département (tester avec 3 ou 4 départements)
# 3) Rassembler les résultats pour trouver le max global
class FileExtractor:
   __FIELDS = ["name", "zipcode", "long", "lat"]

   def __init__(self, zipfile: str, csvfile: str):
      self.__zipfile = zipfile
      self.__csvfile = csvfile

   def __extract_department(self, zipcode: str) -> str:
      if zipcode[:2] != "97":
         pos = zipcode.find('-')
         return zipcode[:pos-3] if pos != -1 else zipcode[:-3]
      else: return zipcode[:-2]

   def extract_data(self) -> dict:
      data = {}

      with ZipFile(self.__zipfile) as zipfile:
         with zipfile.open(self.__csvfile) as csvfile:
            for line in csvfile:
               line = line.decode("utf8").strip().split(',')
               department = self.__extract_department(line[1] if len(line[1]) >= 5 else '0' + line[1])
               if department not in data: data[department] = [dict(zip(self.__FIELDS, [line[0], line[1], line[2], line[3]]))]
               else: data[department].append(dict(zip(self.__FIELDS, [line[0], line[1], line[2], line[3]])))
      return data

def distance_calculator_worker(cities):
    max_distance, it = 0, ""
    for c1, c2 in combinations(cities, r=2):
        d =  geodesic((float(c1["lat"]), float(c1["long"])), (float(c2["lat"]), float(c2["long"]))).km
        if d > max_distance:
            max_distance = d
            it = f"{c1['name']} => {c2['name']}"
            print("new max", it, max_distance)
    return it, max_distance

if __name__ == "__main__":
   fileextractor = FileExtractor("villes_france.zip", "villes_france.csv")
   data = fileextractor.extract_data()
   with Pool(processes=cpu_count() - 1) as pool:
      # Calculate distances
      # ("03", "33", "29", "976", "15")
      distances = pool.map(distance_calculator_worker, [data[dpt] for dpt in ("03", "15", "29")])
      # Sort distances
      distances.sort(key=lambda t: t[1], reverse=True)
      print(distances[0])
# %%
# %%
# %%
print(geodesic((48.1823, 3.97223), (48.4581, -5.09555)).km)
# %%
