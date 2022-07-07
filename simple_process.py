# %%
import os
from time import sleep
from multiprocessing import Process


def worker(n):
    print(f"child: pid {os.getpid()}")
    for i in range(n):
        print(i**2)
        sleep(1)
    # en multiprocess, 
    # a priori le worker ne retourne rien!!


def routine():
    print("do something meanwhile !!")
    sleep(1)

# dans jupyter, le lancement de process / thread
# doit impérativement se faire dans __name__ == "__main__" !!!
if __name__ == "__main__":
    print(f"parent: pid {os.getpid()}")
    p = Process(
        # fonction contenant le code du process enfant
        target=worker, 
        # argument du worker
        args=(5,),
        # nom du process
        name="worker-1",
        # group de process
        # théorie => associé à un PGID
        # permettant de gérer les envois de signaux
        # et fermeture via kill ou pkill
        # dans Python: pas implémenté, donc valeur à None
        # systématiquement !! (idem thread)
        group=None,
        # si True, le parent cherchera à terminer le worker
        # avant de terminer lui même
        daemon=None)
    
    # démarrage du process: fork(UNIX) ou spawn(WIN)
    p.start()

    ## attente synchrone (bloquante) de la fin du worker
    # p.join()
    
    ## attente synchrone avec timeout
    # p.join(3)
    # # terminaison soft
    # p.terminate()
    # # terminaison hard
    # # p.kill()
    # p.join()

    ## attente asynchrone (non bloquante)
    while p.is_alive():
        routine()
    
    
    print(f"{p.name} exited with code {p.exitcode}")

    ## on ne peut pas redémarrer un process !!

    ## tentative de libération de la mémoire d'un process
    # plante si le process tourne toujours !!!!
    # => toujours après un join
    p.close()
# %%
