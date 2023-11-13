from concurrent.futures import ThreadPoolExecutor as poolExecutor
import queue, time

import generate, take

# キューを作成
queue_01 = queue.Queue()
generater = generate.Generater()
taker = take.Taker()

# 処理A
def process_A():
    while True:
        queue_01.put(generater.do())

# 処理B
def process_B():
    while True:
        time.sleep(1)
        if not queue_01.empty():
            data = queue_01.get()
            taker.do(data)

# concurrent.futuresを使用して並列に処理を実行
def main():
    with poolExecutor() as executor:
        future_A = executor.submit(process_A)
        future_B = executor.submit(process_B)

    # 処理Aと処理Bの終了を待つ
    future_A.result()
    future_B.result()

    print("プログラムが終了しました")

if __name__ == "__main__":
    main()