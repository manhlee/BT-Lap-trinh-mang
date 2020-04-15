import socket

def getInfor():
    global HOST_NAME
    HOST_NAME=socket.gethostname()
    global HOST_ADDRESS
    HOST_ADDRESS=socket.gethostbyname(HOST_NAME)
    print(HOST_NAME)
    print(HOST_ADDRESS)
def choosePort():
    global PORT
    PORT=int(input("Nhập cổng giao tiếp:"))
def change_message(message):
    if message=='0':
        return 'zero'
    elif message=='1':
        return 'one'
    elif message=='2':
        return 'two'
    elif message=='3':
        return 'three'
    elif message=='4':
        return 'four'
    elif message=='5':
        return 'five'
    elif message=='6':
        return 'six'
    elif message=='7':
        return 'seven'
    elif message=='8':
        return 'eight'
    elif message=='9':
        return 'nine'
    else:
        return ''        

def creatServer():
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    soc.bind((HOST_ADDRESS,PORT))
    soc.listen(5)
    while True:
        clientConnection,clientAddr=soc.accept()
        print("Kết nối tới máy khách:",clientAddr)
        # content="Xin chào client!!"
        # clientConnection.send(content.encode())
        while True:
            content2=clientConnection.recv(1024).decode()
            print(content2)
            content2=change_message(content2)
            if content2!='':
                clientConnection.send(content2.encode())
            else:
                content3="Ngắt kết nối!"
                clientConnection.send(content3.encode())
                soc.close()
getInfor()
choosePort()
creatServer()