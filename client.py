import socket


#===========================================================================================
DISCONNECTED_MSG = "!close"
SIZE = 1034
IP = socket.gethostbyname(socket.gethostname())  # getting IP address it is str type
PORT = 9999
FORMAT = 'utf-8'
ADDR = (IP, PORT)  # tuple type


#===========================================================================================
# creating socket and binding and listening
def fn_clientConnect(nIP=IP, nPort=PORT):
    # print("main display" +IP)
    global client
    print("[Starting] Client is starting")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[Connected Client ....{nIP}:{nPort}]")

    connected = True
    while connected:
        msg = input('> ')
        client.send(msg.encode(FORMAT))
        if msg == DISCONNECTED_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            msg = f"Server Msg: {msg}"
            print(msg)

#===========================================================================================

def main(nIP=IP, nPort=PORT):
    fn_clientConnect(nIP, nPort)

#===========================================================================================
if __name__ == "__main__":
    main(IP, PORT)
#===========================================================================================
