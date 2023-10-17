import socket
import threading
from queue import Queue

target = "127.0.0.1" #localhost
queue = Queue()
openports = []

def pscan(port): #checks wether the port os open or closed, via establishing a connection
    try:
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock1.connect((target,port))
        return True # if true the port scanner is successful and a port is open
    except:
        return False
    
# print(pscan(443)) 

# for port in range(1, 1024):
#     res = pscan(port)
#     if res:
#         print("port {} is open".format(port))
#     else:
#         print("port {} is closed".format(port))
        
def fill_in_queue(port_list):
    for port in port_list:
        queue.put(port)

def port_scan():
    port = queue.get()
    if pscan(port):
        print("port {} is open".format(port))
        openports.append(port)
        
port_list = range(0,1024)
fill_in_queue(port_list)  

thread_list = []

for i in range(10):
    t = threading.Thread(target = port_scan)
    thread_list.append(t)

for t in thread_list:
    t.start()

print("open ports are", openports)


        

