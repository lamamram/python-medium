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
    __FIELDS = ("id", "firstname", "lastname", "email", "status")

    def __init__(self, model):
        self.model = model
        self.__db = SqliteDb(f"{model}.db")
    
    def get_model(self, _id):
        with self.__db:
            return self.__db.execute(f"SELECT * FROM {self.model}s WHERE id={_id}")
    
    def add_model(self, model_data):
        with self.__db:
            return self.__db.insert(self.model, self.__FIELDS, model_data)


class UserDbAdapter:
    @staticmethod
    def from_api_user(user_data):
        fn, ln = user_data["name"].split()
        st = 1 if user_data["status"] == "active" else 0
        return [
            user_data["id"], 
            ln, fn, user_data["email"], st, 
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")]



if __name__ == "__main__":
    # impossible d'instancier une classe abstraite
    # impossible d'instancier une classe concrète
    # tant qu'elle n'a pas surdéfini les méthodes abstraites
    a = ApiFactory("users")
    response = a.get_model(649)
    if response["valid"]:
        user = response["response"]
        print(user)
        adapted = UserDbAdapter.from_api_user(user)
        # print(adapted)
        db = DbFactory("users")
        db.add_model(adapted)
# %%