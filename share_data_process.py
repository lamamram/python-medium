from multiprocessing import Process, Value, Array, Lock, Manager, current_process
from time import sleep

def worker_share(s, v, l: Lock):
    # placement du verrou: aucun autre process
    # ne peut accéder au worker, tant que le verrou
    # n'est pas levé
    # l.acquire()
    with l:
        print(f" process: {current_process().name}")
        s.value += 10
        # attention, les arrays ont une taille fixe
        _str = v.value.decode("utf8")
        v.value = bytes(_str[::-1], "utf8")
        sleep(2)
    # l.release()

def worker_manager(d, lst, l):
    with l:
        d["k"] = "v"
        lst.reverse()


if __name__ == "__main__":
    # int scalar = 10;
    # 'c': ctypes.c_char,     'u': ctypes.c_wchar,
    # 'b': ctypes.c_byte,     'B': ctypes.c_ubyte,
    # 'h': ctypes.c_short,    'H': ctypes.c_ushort,
    # 'i': ctypes.c_int,      'I': ctypes.c_uint,
    # 'l': ctypes.c_long,     'L': ctypes.c_ulong,
    # 'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
    # 'f': ctypes.c_float,    'd': ctypes.c_double
    scalar = Value("i", 10)
    # vector = Array("c", bytes("bonjour", "utf8"))
    vector = Array("c", b"bonjour")
    lock = Lock()

    # scalar et vector sont écris sur des segments de mémoire partagée
    print("before")
    print(f"scalar: {scalar.value}", f"array: {vector.value.decode('utf8')}")
    procs = [ Process(target=worker_share, args=(scalar, vector, lock), name=f"p-{i}") for i in range(2) ]
    for p in procs: p.start()
    for p in procs: p.join()
    print("after")
    print(f"scalar: {scalar.value}", f"array: {vector.value.decode('utf8')}")

    # surcouche python: gestionnaire de session 
    # partagé par les process python
    # plus lent, mais plus pratique
    with Manager() as mng:
        dico = mng.dict()
        lst = mng.list(range(10))
        lock = mng.Lock()

        m = Process(target=worker_manager, args=(dico, lst, lock))
        m.start();m.join()
        print(dico, lst)
