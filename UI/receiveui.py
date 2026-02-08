from network.peer_socket import create_server
from network.protocol import recv_json,send_json
from transfer.receiver import receive_file
 
RECEIVE_DIR="files/received_files"
def receive_ui():
    port=int(input("listen PORT: "))
    server=create_server(port)
    print("waiting for file request")
    conn,addr=server.accept()
    request=recv_json(conn)
    print(f"\n Incoming from {addr[0]}")
    print(f" FILE:{request['filename']}")
    print(f"Size:{request['filesize']} bytes")
    choice=input("Accept? (y/n): ").lower()
    if choice!="y":
        send_json(conn,{"type":'REJECT'})
        conn.close()
        server.close()
        return
    send_json(conn,{"type":'ACCEPT'})
    print("ACCEPTED. Press P to pause, R to resume, Q to cancel")
    receive_file(conn,request["filename"],request["filesize"],RECEIVE_DIR)
    conn.close()
    server.close()