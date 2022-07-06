from abc import ABC, abstractmethod
import json

class AbsFactory(ABC):
    @abstractmethod
    def get_model(self, _id):
        pass

class JsonFactory(AbsFactory):

    __EXT = ".json"

    def __init__(self, model, models_path="models/"):
        self.__MODELS_PATH = models_path
        self._file = self.__MODELS_PATH + model + self.__EXT
    
    def get_model(self, _id):
        with open(self._file) as f:
            return json.loads(f.read())[str(_id)]

class FactoryStore:

    def __init__(self):
        self._factories = {}

    def register_source(self, source, factory_class):
        self._factories[source] = factory_class

    def get_factory(self, source, model):
        factory = self._factories.get(source)
        if not factory:
            raise ValueError("{source} not implemented !")
        return factory(model)

store = FactoryStore()
store.register_source('json', JsonFactory)


if __name__ == "__main__":
    pass

