from multiprocessing import Process, Queue, cpu_count, current_process
import queue, os

def worker(q_in: Queue, q_out: Queue):
    tries = NB_TASKS
    while True:
        try:
            # acquisition des tâches en mode non bloquant
            task = q_in.get(False, timeout=0.1)
            print(f"{task} acquired by {current_process().name}")
        except queue.Empty:
            if not tries:
                print(f"{current_process().name} broke !")
                break
            tries -= 1
        else:
            q_out.put(f"{task} dealt by {current_process().name}")

        

NB_TASKS = 500
NB_WORKERS = cpu_count() - 2

if __name__ == "__main__":
    q_in, q_out = Queue(), Queue()
    for i in range(NB_TASKS):
        q_in.put(f'task_{i}')
    
    procs = [ Process (target=worker, args=(q_in, q_out)) for _ in range(NB_WORKERS)]
    for p in procs: p.start()
    for p in procs:
        # on doit commmencer à vider q_out pour vider son buffer interne 
        while p.is_alive():
            p.join(2)
            while not q_out.empty():
                print(q_out.get(False))

            
