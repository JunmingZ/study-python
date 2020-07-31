import threading

# 创建全局变量
global_list = []


# 添加数据
def add_data():
    print('追加的线程：', threading.current_thread())
    for i in range(5):
        # 在末尾追加
        global_list.append(i)
    print('追加的线程：', global_list)


# 读取数据
def read_data():
    print('读取的线程：', threading.current_thread())
    print('读取的线程：', global_list)


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)
    # 开启添加数据
    add_thread.start()
    # 线程等待
    add_thread.join()
    read_thread.start()

"""
追加的线程： <Thread(Thread-1, started 18396)>
追加的线程： [0, 1, 2, 3, 4]
读取的线程： <Thread(Thread-2, started 16288)>
读取的线程： [0, 1, 2, 3, 4]
"""