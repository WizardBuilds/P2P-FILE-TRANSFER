import os
from network.peer_socket import connect_peer
from network.protocol import send_json,recv_json
from transfer.sender import send_files

Shared_Dir="files/shared_files"
def send_ui():
    files=os.listdir(Shared_Dir)
    if not files:
        print("No files to send!!")
        return
    print("\n Select file:")
    for i,f in enumerate(files):# it is used for accessing the index and file
        size=os.path.getsize(os.path.join(Shared_Dir,f))
        print(f"[{i+1}] {f} ({size} bytes)")
    idx=int(input("Choice: "))-1
    filename=files[idx]
    filepath=os.path.join(Shared_Dir,filename)
    filesize=os.path.getsize(filepath)
    ip=input("RECEIVER Ip address: ")
    port=int((input("RECEIVER PORT: ")))
    sock=connect_peer(ip,port)
    send_json(sock,{"type":"FILE REQUEST","filename":filename,"filesize":filesize})
    response=recv_json(sock)
    if response["type"]!="ACCEPT":
        print("Receiver rejected the request")
        sock.close()
        return
    print("RECEIVER accepted. Start transfer. Press P to pause, R to resume, Q to cancel")
    send_files(sock,filepath)
    sock.close()