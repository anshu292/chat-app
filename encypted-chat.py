import socket
import threading
import rsa

public_key,private_key=rsa.newKeys(1024)

choice=input("Do you want to host (1) or connect (2)")

if(choice=="1"):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind("10.100.83.1",12345)
    server.listen()

    client,_=server.accept()

    client.send(public_key.save_pkcs1("PEM"))
    public_partner=rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice=="2":
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("10.100.83.1",12345))
    public_partner=rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
else:
    exit()
    # invald command

def sending_messages(c):
    while True:
        message=input("")
        c.send(rsa.encrpt(message.encode(),public_partner))
        print("You "+message)



def receiving_messages(c):
    while True:
        print("Partner: "+rsa.decrypt(c.recv(1024).decode(),private_key).decode())


threading.Thread(target=sending_messages,args=(client,)).start()
threading.Thread(target=receiving_messages,args=(client,)).start()



