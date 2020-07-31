import threading
import time

# 创建互斥锁
lock = threading.Lock()


# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def get_value(index):

    # 上锁
    lock.acquire()
    print(threading.current_thread())
    my_list = [3,6,8,1]
    # 判断下标释放越界
    if index >= len(my_list):
        print("下标越界:", index)
        return
    value = my_list[index]
    print(value)
    time.sleep(0.2)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for i in range(30):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()

"""
<Thread(Thread-1, started 13880)>
3
<Thread(Thread-2, started 14572)>
6
<Thread(Thread-3, started 16972)>
8
<Thread(Thread-4, started 16224)>
1
<Thread(Thread-5, started 12356)>
下标越界: 4
一直等待响应
"""