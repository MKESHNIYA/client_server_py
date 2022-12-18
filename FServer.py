import socket
import threading
import sys


#===========================================================================================
DISCONNECTED_MSG = "!close"
SIZE = 1024
IP = socket.gethostbyname(socket.gethostname()) # getting IP address it is str type
PORT = 9999
ADDR = (IP, PORT) #tuple type
FORMAT = 'utf-8'

#===========================================================================================
#creating socket and binding and listening
def fn_socketBindListening(nIP=IP, nPort=PORT):
    #print("main display" +IP)
    print("[Starting] Server is starting")
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen(1)
        print(f"[Server Assigned Port to Listening Client:....{nIP}:{nPort}]")
    except socket.error as msg :
        print("Error while Socket creation,Binding and Listening "+str(msg))
        sys.exit()


#===========================================================================================
#Accepting request from clint and creating thread for each client and handed over to client handler fun
def fn_accepting():
    print("accepting")

    try:
            while True:
                conn, addr = server.accept() #addr[0] is ip and str type and addr[1] is port int type..
                #print("addr",addr[0],"....port"+str(addr[1]))
                thread = threading.Thread(target= fn_clientHandler, args=(conn,addr))
                thread.daemon = True #free the server resources while closeing of theread
                thread.start()
                print(f"ACTIVE Client  {threading.active_count()-1}")
    except threading.ThreadError as msg :
        print("Error while Thread creation "+str(msg))
        sys.exit()
    except socket.error as msg:
        print("Error while Thread creation " + str(msg))
        sys.exit()

#===========================================================================================
#fun to handle each client from server side
def fn_clientHandler(conn, addr):
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECTED_MSG:
            connected = False
        print(f"At Server[{addr}]--{msg}")
        msg=f"Received Msg: {msg}"
        conn.send(msg.encode(FORMAT))
    conn.close()
    
#===========================================================================================
def main(nIP=IP, nPort=PORT):
    fn_socketBindListening(nIP, nPort)
    fn_accepting()

#===========================================================================================
if __name__== "__main__":
    main(IP, PORT)
#===========================================================================================
