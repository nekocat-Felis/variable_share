from concurrent.futures import ThreadPoolExecutor as poolExe
import queue

#import generate, take

job_queue = queue.Queue()
generater = generate.Generater(job_queue)
taker = take.Taker(job_queue)

def gen_run():
    i = 0
    while True:
        job_queue.put(i)
        i += 1


def tak_run():
    while True:
        print(self.queue.get())

with poolExe() as pool:
    pool.map([gen_run, tak_run])
