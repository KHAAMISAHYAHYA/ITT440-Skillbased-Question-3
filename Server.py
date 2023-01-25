import socket
import threading
import random

quotes = ["Beauty begins the moment you decide to be yourself. (Coco Chanel)", "Happiness and confidence are the prettiest things you can wear. (Taylor Swift)", "Beautiful people are not always good but good people are always beautiful. (Imam Ali)", "Beauty comes from knowing who you actually are. (Ellen DeGeneres)", "Don't be afraid to speak up for yourself. Keep fighting for your dreams. (Gabby Douglas)", "If you are always trying to be normal, you will never know how amazing you can be. (Maya Angelou)"]

def quote(clientsocket):
  rquote = random.choice(quotes)
  clientsocket.sendall (rquote.encode())
  clientsocket.close()
  
def main():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(("192.168.6.128", 8888))
  s.listen (5)
  
  while True:
    csock, addr = s.accept()
    print ("Got a connection from %s" % str(addr))
    chandler - threading.Thread(target = quote, args = (csock, ))
    chandler.start()
    
main()
