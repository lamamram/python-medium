from time import perf_counter, sleep

def chrono(f):
    def wrapper(*a, **kw):
        start = perf_counter()
        ret = f(*a, **kw)
        print(f"{perf_counter() - start:.3f} s")
        return ret
    return wrapper