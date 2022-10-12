from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    try: 
        message = "Random string of words"
        clientSocket.sendto(message.encode(),('127.0.0.1', 2022))
        clientSocket.settimeout(20)
        modifiedMessage, serverAddress = clientSocket.recvfrom(2022)
        print(modifiedMessage.decode())
    except clientSocket.timeout: 
        print("Error timeout")
        clientSocket.close()    