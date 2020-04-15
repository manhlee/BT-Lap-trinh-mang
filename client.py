import socket
def chooseServer():
    global SERVER_ADDRESS
    SERVER_ADDRESS=input("Nhập vào server kết nối tới:")
    global PORT
    PORT=int(input("Nhập vào cổng kết nối:"))
def createClient():
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    soc.connect((SERVER_ADDRESS,PORT))
    message=''
    while message!='END':
        message=str(input("Nhập tin nhắn:"))
        soc.send(message.encode())
        content3=soc.recv(1024).decode()
        print(content3)

chooseServer()
createClient()