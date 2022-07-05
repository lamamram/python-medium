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

# le bloc d'instruciton s'exécute dans try mis en place par 
# __enter__
# une exception sera capturée dans __exit__ (comme la classe Exception)
with Ctx("param") as c:
    print("block")
    print(c.param)
    3/0

    
# %%
# contexte réentrant
import os

project_path = os.path.dirname(__file__)
project_path = os.path.abspath("")


class Cd:
    def __init__(self, path) -> None:
        self.path = path
    
    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, x_type, x_msg, x_tb):
        os.chdir(self.old_path)

print("enter dir")
with Cd(f"{project_path}/dir"):
    print(os.getcwd())
    print("enter subdir")
    with Cd("./subdir"):
        print(os.getcwd())
    print("exit subdir")
    print(os.getcwd())
print("exit dir")
print(os.getcwd())


# %%
