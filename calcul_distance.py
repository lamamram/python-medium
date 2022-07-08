"""
but calculer la distance max entre 2 villes
d'un même dept en France
"""
# %%
import os
import pandas as pd
import numpy as np
from itertools import combinations
from multiprocessing import Pool, cpu_count
# distance geodésique
# pip install geopy
from geopy.distance import geodesic


# trouver le dept à partir du zipcode
def get_dept(elem):
    return "0" + elem[0] if len(elem) == 4 else elem[0:2]


# calcul de distance max pour 1 dept
def get_max_geodesic(df):
    # retourne un tuple qui contient 
    # l'itinéraire et la distance max
    max_distance, it = 0, ""
    # combinaison de lignes du df
    for i1, i2 in combinations(df.index, r=2):
        row1, row2 = df.loc[i1], df.loc[i2]
        p1, p2 = (row1["lat"], row1["lon"]), (row2["lat"], row2["lon"])
        d = geodesic(p1, p2).km
        if d > max_distance:
            max_distance = d
            it = f"{i1} <-> {i2}"
    return it, max_distance

def process():
    with Pool(processes=cpu_count() // 2 + 2) as pool:
        depts = ["01", "03", "15", "29", "33", "92"]
        dfs = [villes_df[villes_df["dept"] == dept] for dept in depts]
        distances = pool.map(get_max_geodesic, dfs)
        
        # traitemnt post
        results = dict(zip(depts, distances))
        print(results)
        results = sorted(results.items(), key=lambda r: r[1][1], reverse=True)
        print(results[0])



if __name__ == "__main__":
    if not os.path.exists("villes_dept.zip"):
        villes_df = pd.read_csv(
            "villes_france.zip",
            encoding="iso-8859-1",
            # pas de colonnes
            header=None,
        )
        villes_df.columns = pd.Index(["name", "zipcode", "lon", "lat"])
        villes_df["dept"] = villes_df["zipcode"].apply(get_dept)
        villes_df.set_index("name", inplace=True)
        villes_df.to_csv(
            "villes_dept.zip",
            compression={
                "method": "zip",
                "archive_name": "villes_dept.csv"
            }
        )
    else:
        villes_df = pd.read_csv(
            "villes_dept.zip",
            index_col="name",
            dtype={
                "dept": object
            }
        )
        # print(villes_df)
        # print(villes_df.dtypes)
    
    # df = villes_df[villes_df["dept"] == "03"]
    # print(get_max_geodesic(df))
    process()
# %%
# %%
