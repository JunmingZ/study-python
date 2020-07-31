import threading
import time


# 唱歌任务
def sing():
    # 获取当前线程
    print("sing当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print(f"正在唱歌...{i}")
        time.sleep(1)


# 跳舞任务
def dance():
    # 扩展： 获取当前线程
    print("dance当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print(f"正在跳舞...{i}")
        time.sleep(1)


if __name__ == '__main__':
    # 获取当前线程
    print("当前执行的线程为：", threading.current_thread())
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    # 开启线程
    sing_thread.start()
    dance_thread.start()

"""
当前执行的线程为： <_MainThread(MainThread, started 9884)>
sing当前执行的线程为： <Thread(Thread-1, started 11932)>
正在唱歌...0
dance当前执行的线程为： <Thread(Thread-2, started 11060)>
正在跳舞...0
正在唱歌...1
正在跳舞...1
正在唱歌...2
正在跳舞...2
"""
