import socket
import sys
import subprocess

server    = raw_input("Enter a remote host to scan: ")
serverIP  = socket.gethostbyname(server)

print "Please wait, scanning remote host,", serverIP, "This may take some time."


#Scanning some basic ports
#Append other ports to scan
ports= [80,22,21,23,25,26,53,161,443,3306,15,110] 

try:
    for port in ports:  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverIP, port))
        if result == 0:
            print "Port {}: Open".format(port)
        sock.close()
        if result != 0:
            print "Port {}: Closed".format(port)
        sock.close()


except socket.gaierror:
    print 'Hostname could not be resolved.'
    sys.exit()

except socket.error:
    print "Couldn't connect to server."
    sys.exit()


print 'Scanning Completed"
