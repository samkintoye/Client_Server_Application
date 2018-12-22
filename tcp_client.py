import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "localhost"              #Server IP address
port = 50000                    # port number

s.connect((host, port))
s.send("good day server!")

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
