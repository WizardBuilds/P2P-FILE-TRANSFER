import json
def send_json(sock,data):
    msg=json.dumps(data).encode()
    sock.sendall(len(msg).to_bytes(4,"big")+msg)
def recv_json(sock):
    length=int.from_bytes(sock.recv(4),"big")
    data=sock.recv(length)
    return json.loads(data.decode())