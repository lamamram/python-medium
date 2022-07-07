from multiprocessing import Process
import os, sys
from time import sleep
from signal import signal, SIGTERM, SIGINT, SIG_IGN

def handler(signum, stack):
    print(f"process {os.getpid()} received signal {signum}")
    sys.exit(0)

def worker(n):
    signal(SIGTERM, handler=handler)
    for i in range(n, -1, -1):
        print(i)
        sleep(1)


if __name__ == "__main__":
    print(f"parent pid: {os.getpid()}")
    p = Process(target=worker, args=(5,))
    # désactivation du ctrl + c
    signal(SIGINT, SIG_IGN)
    p.start()
    p.join(3)
    # p.terminate()
    os.kill(p.pid, SIGTERM)
    p.join()

    print(f"{p.name} exited with code {p.exitcode}")