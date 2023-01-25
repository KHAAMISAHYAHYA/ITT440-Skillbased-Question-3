import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.6.128", 8888))
    data = s.recv(1024)
    print ("Quotes of the day: %s" % data.decode())
    s.close()
    
main()
