from concurrent.futures import ThreadPoolExecutor as poolExe
import queue

import generate, take

job_queue = queue.Queue()
generater = generate.Generater(job_queue)
taker = take.Taker(job_queue)

def gen_run():
    generater.run()

def tak_run():
    taker.run()

with poolExe() as pool:
    pool.map([gen_run, tak_run])
