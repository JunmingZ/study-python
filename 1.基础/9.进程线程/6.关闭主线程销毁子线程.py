"""
关闭主线程销毁子线程需要设置线程守护
方式一：threading.Thread(target=show_info, daemon=True)
方式二：线程对象.setDaemon(True)
"""

import threading
import time


# 测试主线程是否会等待子线程执行完成以后程序再退出
def show_info():
    for i in range(5):
        print("test:", i)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建子线程守护主线程
    # daemon=True 守护主线程
    # 守护主线程方式1
    sub_thread = threading.Thread(target=show_info, daemon=True)
    # 设置成为守护主线程，主线程退出后子线程直接销毁不再执行子线程的代码
    # 守护主线程方式2
    # sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程延时1秒
    time.sleep(1)
    print("over")


"""
test: 0
test: 1
over
"""