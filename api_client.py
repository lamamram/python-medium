# %%
import requests
import json

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

if __name__ == "__main__":
    api = GoRestApi()
    obj = api.get_user(3213)
    print(obj["response"])

# %%
