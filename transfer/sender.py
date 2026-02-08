import os
import threading
import time
from transfer.chunk_manager import read_chunks
  
def send_files(sock,filepath):
    filesize=os.path.getsize(filepath)
    sent=0
    pause_event=threading.Event()
    pause_event.set()
    stop_flag={"stop":False}
    def input_listener():
     while True:
        key=input().lower()
        if key=="p":
            pause_event.clear()
            print("\n PAUSED")
        elif key=="q":
            stop_flag["stop"]=True
            pause_event.set()
            print("\n Transfer cancelled")
            break
    threading.Thread(target=input_listener,daemon=True).start()
    with open(filepath,"rb") as f:
       while not stop_flag["stop"]:
          pause_event.wait()
          chunk=f.read(4096)
          if not chunk:
            break
          sock.sendall(chunk)
          sent+=len(chunk)
          percent=(sent/filesize)*100
          print(f"\r Sending:{percent:.2f}%",end="")
          time.sleep(0.01)
    if not stop_flag["stop"]:
      print("\n Sucessfully transferred")