# %%
import requests
import json
from decorators import chrono
from concurrent.futures import ThreadPoolExecutor as TPE, as_completed

class GoRestApi:
    __URL = "https://gorest.co.in/public"

    def __init__(self, version="v2", encoding="utf8") -> None:
        self.__version = version
        self.__session = requests.Session()
        self.__encoding = encoding

    def __call(self, method, endpoint, *, data={}, headers={}, files={}):
        """
        méthode privé de manipulation de requests
        """
        url = f"{self.__URL}/{self.__version}/{endpoint}"
        try:
            r = self.__session.send(requests.Request(
                method.upper(), url=url, data=data, headers=headers, files=files).prepare())
            # gestion code retour http
            if  200 <= r.status_code < 300:
                # gestion du content-type
                if "application/json" in r.headers["content-type"]:
                    response = r.json()
                    # gestion de l'encodage
                    if self.__encoding != r.encoding:
                        response = r.text.encode(self.__encoding)
                        response = json.loads(response)
                    return {"valid": True, "response": response}
            raise ValueError(f"wrong status: {r.status_code}: {r.text}")
        # remontée des erreurs
        except (requests.ConnectionError, requests.HTTPError, ValueError) as e:
            return {"valid": False, "response": e}

    def get_users(self, user_id):
        """
        méthode publique: télécharge un user
        """
        return self.__call("GET", f"users/{user_id}")
    
    def get_page(self, page_id):
        return self.__call("GET", f"users?page={page_id}")
    
    @chrono
    def get_all_users(self, nb_workers=2, limit=10):
        data = []
        with TPE(max_workers=nb_workers) as pool:
            # on peut travailler sur les réponse
            # au fur et à mesure
            futs = [pool.submit(self.get_page, i) for i in range(1, limit + 1)]
            for f in as_completed(futs):
                data.append(f.result())
            # données d'un coup
            # data = pool.map(self.get_page, list(range(1, limit + 1)))
            print(f"pages 1 to {limit} fetched")
            return data
                


@chrono
def sequential(api, nb_page=100):
    data = []
    for i in range(1, nb_page + 1):
        r = api.get_page(i)
        print(f"page {i} fetched")
        if r["valid"]: data += r["response"]
    return data

if __name__ == "__main__":
    api = GoRestApi()
    # obj = api.get_user(3213)
    # sequential(api)
    data = api.get_all_users(nb_workers=10, limit=100)
    print(data)

# %%
# %%
