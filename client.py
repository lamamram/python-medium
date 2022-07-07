# %%
from factory import *


class User:
    __model = "users"
    __FIELDS = ("id", "firstname", "lastname", "email", "status", "created_at")

    def __init__(self, _id, source="db") -> None:
        data = store.get_factory(source, self.__model).get_model(_id)
        if data["valid"]:
            data = getattr(UserAdapter, f"from_{source}")(data["response"])
            for f in self.__FIELDS:
                setattr(self, f, data[f])
        else: raise ValueError(data["response"])


    def __str__(self) -> str:
        pass

    # manipuler les champs de l'utilisateur
    def get_full_name(self):
        return f"{self.firstname.capitalize()} {self.lastname.upper()}"

if __name__ == "__main__":
    u = User(649)
    print(u.get_full_name())
# %%
