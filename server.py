import socket

# Create an internet socket INET and it's a stream base socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local host with the port 9999
server.bind(('localhost', 9999))

server.listen()

# Accept incoming connections
client, addr = server.accept()

done = False

while not done:
    # Recieve and decode what we get from the client
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print(msg)
    # Send a message to the client
    client.send(input("Message: ").encode('utf-8'))

# Close the socket
client.close()
server.close()