# %%
# classe contexte
from traceback import print_tb

class Ctx:
    def __init__(self, param) -> None:
        self.param = param
    
    def __enter__(self):
        print("enter")
        return self
    
    def __exit__(self, x_type, x_msg, x_tb):
        print("exit")
        print(x_type, x_msg)
        print_tb(x_tb)
        # retourner une valeur vraie
        # intercepte l'exception
        return True


with Ctx("param") as c:
    print("block")
    print(c.param)
    3/0


    
# %%
