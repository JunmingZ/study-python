import socket

if __name__ == '__main__':
    """
    创建tcp客户端套接字
    AF_INET：表示ipv4
    SOCK_STREAM: tcp传输协议
    """
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 和服务端应用程序建立连接
    tcp_client_socket.connect(("192.168.3.9", 8080))

    # 准备发送的数据
    send_data = "你好服务端，我是客户端小黑!".encode("gbk")
    print('将要发送已编码成gbk的数据：', send_data)

    # 发送数据
    tcp_client_socket.send(send_data)

    # 接收数据, 这次接收的数据最大字节数是1024
    recv_data = tcp_client_socket.recv(1024)

    # 返回的直接是服务端程序发送的二进制数据
    print('服务端返回的数据', recv_data)

    # 对数据进行解码
    recv_content = recv_data.decode("gbk")
    print("接收服务端解码后的数据为:", recv_content)

    # 关闭套接字
    tcp_client_socket.close()


"""
将要发送已编码成gbk的数据： b'\xc4\xe3\xba\xc3\xb7\xfe\xce\xf1\xb6\xcb\xa3\xac\xce\xd2\xca\xc7\xbf\xcd\xbb\xa7\xb6\xcb\xd0\xa1\xba\xda!'
服务端返回的数据 b'\xce\xd2\xca\xc7\xb7\xfe\xce\xf1\xc6\xf7'
接收服务端解码后的数据为: 我是服务器
"""