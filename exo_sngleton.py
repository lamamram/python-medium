# %%

class Single:
    __instance = None

    def __init__(self) -> None:
        if self.__instance != None:
            raise TypeError("already instantiated !!")
        Single.__instance = self

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance



s = Single.get_instance()
s2 = Single.get_instance()
s3 = Single()

s is s2
s is s3
# %%
