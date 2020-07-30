import multiprocessing
import os


def dance():
    # 获取当前进程的编号
    print("dance:", os.getpid())
    # 获取当前进程
    # multiprocessing.current_process返回与当前进程对应的进程对象
    print("dance:", multiprocessing.current_process())
    for i in range(5):
        print(f"跳舞中...{i}")
        # 扩展:根据进程编号杀死指定进程
        os.kill(os.getpid(), 9)


if __name__ == '__main__':
    # 获取当前进程的编号
    print("main:", os.getpid())
    # 获取当前进程
    print("main:", multiprocessing.current_process())
    dance_process = multiprocessing.Process(target=dance, name="myprocess1")
    # 启动子进程执行对应的任务
    dance_process.start()

"""
main: 16040
main: <_MainProcess name='MainProcess' parent=None started>
dance: 15900
dance: <Process name='myprocess1' parent=16040 started>
跳舞中...0
"""