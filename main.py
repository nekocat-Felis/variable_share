from concurrent.futures import ThreadPoolExecutor as poolExe
import queue

import generate, take

job_queue = queue.Queue()

generater = generate.Generater(job_queue)
taker = take.Taker(job_queue)

with poolExe() as pool:
    pool.map([generater.run, taker.run])