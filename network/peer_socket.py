import socket
def create_server(port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#tcp connection for socket
    s.bind(("",port))
    s.listen(5)
    return s
def connect_peer(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    return s