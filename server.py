import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 4445))
    server.listen(1)
    print('Try to connect...')
    client, addr = server.accept()
    print(f"Connection established with: {addr}")
    while True:
        command = input(">")
        if command.lower() == 'exit':
            break
        client.send(command.encode())
        result = client.recv(2096).decode()
        print(result)
    client.close()
    server.close()

if __name__ == '__main__':
    main()
