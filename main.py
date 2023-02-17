from socket import *

server_Sock = socket(AF_INET, SOCK_STREAM)
server_Port = 3248
server_Sock.bind(("192.168.0.116", server_Port))
server_Sock.listen(10)

while True:
    print("READY TO START THE SERVER!......")
    connectionSocket, address = server_Sock.accept()
    try:
        msg = connectionSocket.recv(1024)
        file_name = msg.split() [1]
        fn = open(file_name[1:])
        out_data = fn.read()
        print(type(out_data))
        out_data = bytes(out_data, 'utf-8')
        print(type(out_data))

        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
        # for content in range(0, len(out_data)):
        #     connectionSocket.send(out_data[content])
        connectionSocket.send(out_data)
        connectionSocket.send(b'\r\n')

        connectionSocket.close()

    except IOError:
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.send(b'<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')
        connectionSocket.close()