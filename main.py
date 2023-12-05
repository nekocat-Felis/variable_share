from concurrent.futures import ThreadPoolExecutor as poolExecutor
import queue, time

import generate, take

# キューを作成
queue_01 = queue.Queue()
generater = generate.Generater(queue_01)
taker = take.Taker(queue_01)

# concurrent.futuresを使用して並列に処理を実行
def main():
    with poolExecutor() as executor:
        future_A = executor.submit(generater.do)
        future_B = executor.submit(taker.do)

    # 処理Aと処理Bの終了を待つ
    future_A.result()
    future_B.result()

    print("プログラムが終了しました")

if __name__ == "__main__":
    main()