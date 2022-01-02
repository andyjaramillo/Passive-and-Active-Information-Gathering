import socket

sock_ = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock_.connect((socket.gethostname(),8080))
msg = sock_.recv(1024)
sock_.close()
print(msg.decode("ascii"))
