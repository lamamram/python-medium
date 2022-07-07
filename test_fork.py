import os, sys
from time import sleep

pid = os.fork()
if pid != 0:
    print("parent: child PID", pid)
else:
    print("child")
    sleep(3)
    print("child exits !")
    sys.exit(0)


while True:
    print("waiting for children")
    try:
        pid, status = os.waitpid(pid, 0)
        print(pid, status)
    except OSError as oe:
        print(oe)
    break