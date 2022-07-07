# %%
from factory import *
import json

class Model:

    def __init__(self, _id, source, model, fields) -> None:
        self.__model = model
        self.__FIELDS = fields
        data = store.get_factory(source, self.__model).get_model(_id)
        if data["valid"]:
            data = getattr(UserAdapter, f"from_{source}")(data["response"])
            for f in self.__FIELDS:
                setattr(self, f, data[f])
        else: raise ValueError(data["response"])

    def __str__(self) -> str:
        attrs = [attr for attr in dir(self) if not attr.startswith("_") and not callable(getattr(self, attr))]
        dct = {attr: getattr(self, attr) for attr in attrs}
        return json.dumps(dct)


class User(Model):
    __model = "users"
    __FIELDS = ("id", "firstname", "lastname", "email", "status", "created_at")

    def __init__(self, _id, source="db"):
        super().__init__(_id, source, self.__model, self.__FIELDS)

    # manipuler les champs de l'utilisateur
    def get_full_name(self):
        return f"{self.firstname.capitalize()} {self.lastname.upper()}"

if __name__ == "__main__":
    u = User(649, "api")
    print(u)
# %%
