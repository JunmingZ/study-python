import socket

if __name__ == '__main__':
    # 创建服务端套接字对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置端口号复用，让程序退出端口号立即释放,解决第二次启动出现端口被占用
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 绑定端口号
    server.bind(("", 8080))

    # 设置监听
    server.listen(128)

    # 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
    # 返回值是一对(conn, address)，其中conn是一个新的套接字对象，可用于在连接上发送和接收数据，而address是绑定到连接另一端套接字的地址。
    service_client_socket, ip_port = server.accept()

    print("接收到客户端的ip地址和端口号:", ip_port)

    # 接收客户端发送的数据, 这次接收数据的最大字节数是1024
    recv_data = service_client_socket.recv(1024)

    # 获取数据的长度
    recv_data_length = len(recv_data)
    print("接收数据的长度为:", recv_data_length)

    # 对二进制数据进行解码
    recv_content = recv_data.decode("gbk")
    print("接收客户端的数据为:", recv_content)

    # 准备发送的数据
    send_data = "ok, 问题正在处理中...".encode("gbk")
    # 发送数据给客户端
    service_client_socket.send(send_data)

    # 关闭服务与客户端的套接字， 终止和客户端通信的服务
    service_client_socket.close()
    # 关闭服务端的套接字, 终止和客户端提供建立连接请求的服务
    server.close()

"""
接收到客户端的ip地址和端口号: ('192.168.132.1', 54600)
接收客户端的数据为: 我是客户端
"""
