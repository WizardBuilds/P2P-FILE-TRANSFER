import os
import threading
import time
from transfer.chunk_manager import chunk_size

def receive_file(sock,filename,filesize,save_dir):
    os.makedirs(save_dir,exist_ok=True)
    path=os.path.join(save_dir,filename)
    received=0
    pause_event=threading.Event()
    pause_event.set()
    stop_flag={"stop":False}
    def input_listener():
        while True:
            key=input().lower
            if key=="p":
                pause_event.clear()
                print("\n PAUSED")
            elif key=="r":
                pause_event.set()
                print("\n RESUMED")
            elif key=="q":
                stop_flag["stop"]=True
                pause_event.set()
                print("\n Transfer Cancelled")
                break
    threading.Thread(target=input_listener,daemon=True).start()# daemon threading for ending with main thread
    with open(path,"wb") as f:
        while received<filesize and not stop_flag["stop"]:
            pause_event.wait()
            chunk=sock.recv(min(4096,filesize-received))
            if not chunk:
                break
            f.write(chunk)
            received+=len(chunk)
            percent=(received/filesize)*100
            print(f"\r Receiving:{percent:.2f}%",end="")
            time.sleep(0.01)
    if not stop_flag["stop"]:
        print("\n Received Sucessfully")


