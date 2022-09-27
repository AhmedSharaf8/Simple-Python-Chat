import socket

# Create an internet socket INET and it's a stream base socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the same host
client.connect(('localhost', 9999))

done = False

while not done:
    client.send(input('Message: ').encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print(msg)

client.close()