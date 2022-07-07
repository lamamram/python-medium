# %%
from abc import ABC, abstractmethod
from datetime import datetime
from api_client import GoRestApi
from db_client import SqliteDb
from datetime import datetime

class AbstractFactory(ABC):
    @abstractmethod
    def __init__(self, model) -> None:
        pass

    @abstractmethod
    def get_model(self, _id):
        pass

    @abstractmethod
    def add_model(self, model_data):
        pass

class ApiFactory(AbstractFactory):
    def __init__(self, model):
        self.__api = GoRestApi()
        self.model = model
    
    def get_model(self, _id):
        call_fn = getattr(self.__api, f"get_{self.model}")
        return call_fn(_id)
    
    def add_model(self, model_data):
        pass

class DbFactory(AbstractFactory):
    __FIELDS = ("id", "firstname", "lastname", "email", "status", "created_at")

    def __init__(self, model):
        self.model = model
        self.__db = SqliteDb(f"{model}.db")
    
    def get_model(self, _id):
        with self.__db:
            return self.__db.execute(f"SELECT * FROM {self.model} WHERE id={_id}", one=True)
    
    def add_model(self, model_data):
        with self.__db:
            return self.__db.insert(self.model, self.__FIELDS, model_data)


# design pattern adapter
class UserAdapter:
    @staticmethod
    def from_api(data):
        fn, ln = data["name"].split()
        st = 1 if data["status"] == "active" else 0
        return {
            "id": data["id"], 
            "lastname": ln, 
            "firstname": fn, 
            "email": data["email"], 
            "status": st, 
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    @staticmethod
    def from_db(data):
        return data


# magasin de factories
class FactoryStore:
    def __init__(self) -> None:
        self.__factories = {}

    def register(self, source, factory_class):
        self.__factories[source] = factory_class

    def get_factory(self, source, model):
        fact = self.__factories.get(source)
        if not fact:
            raise KeyError(f"{source} not registered !")
        return fact(model)


store = FactoryStore()
store.register("db", DbFactory)
store.register("api", ApiFactory)



if __name__ == "__main__":
    # impossible d'instancier une classe abstraite
    # impossible d'instancier une classe concrète
    # tant qu'elle n'a pas surdéfini les méthodes abstraites
    a = ApiFactory("users")
    response = a.get_model(649)
    if response["valid"]:
        user = response["response"]
        adapted = UserAdapter.from_api(user)
        db = DbFactory("users")
        print(db.add_model([adapted]))
    else: print(response["response"])
    db = DbFactory("users")
    print(db.get_model(649))
# %%
# %%
