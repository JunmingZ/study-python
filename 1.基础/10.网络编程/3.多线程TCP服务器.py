import socket
import threading

"""
编写一个TCP服务端程序，循环等待接受客户端的连接请求
当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞
把创建的子线程设置成为守护主线程，防止主线程无法退出。
"""


def handle_request(s_client_socket, ip_port):
    # 接收的数据不确定长度，所以来个死循环
    while True:
        # 接收客户端的数据
        data = s_client_socket.recv(1024)
        if data:
            print('接收的数据：', data.decode('gbk'), ip_port)
            # 回复
            s_client_socket.send('ok, 收到了'.encode('gbk'))
        else:
            print('客户端下线', ip_port)
            break
    # 终止和客户端进行通信
    s_client_socket.close()


def server_star():
    # 创建服务端套接字对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，让程序退出端口号立即释放,解决第二次启动出现端口被占用
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    server.bind(("", 8080))

    # 设置监听
    server.listen(128)

    # 开启死循环
    while True:
        # 等待接收客户端的连接请求
        s_client_socket, ip_port = server.accept()
        print('客户端连接成功:', ip_port)

        # 创建一个子线程，不同子线程负责接收不同客户端的消息
        sub_thread = threading.Thread(target=handle_request, args=(s_client_socket, ip_port))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程
        sub_thread.start()


if __name__ == '__main__':
    # 启用服务器
    server_star()


"""
客户端连接成功: ('192.168.132.1', 51729)
接收的数据： 我是客户端1 ('192.168.132.1', 51729)
客户端连接成功: ('192.168.3.9', 51778)
接收的数据： 我是客户端2 ('192.168.3.9', 51778)
接收的数据： 我是客户端2，测试第二轮发送 ('192.168.3.9', 51778)
接收的数据： 我是客户端2，测试第3轮发送 ('192.168.3.9', 51778)
接收的数据： 我是客户端1，测试第一轮发送 ('192.168.132.1', 51729)
"""