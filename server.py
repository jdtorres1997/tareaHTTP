#!/usr/bin/env python3

import argparse

import sys
import itertools
import socket
from socket import socket as Socket

import httplib
# A simple web server

# Issues:
# Ignores CRLF requirement
# Header must be < 1024 bytes
# ...
# probabaly loads more

#--port <#puerto>

backlog = 5

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    endpoint = ('', args.port)
    
    ss.bind(endpoint)
    ss.listen(backlog)
    print("server ready")

    while True:


         cs = ss.accept()[0] 
         request = cs.recv(1024).decode('ascii')
	 print request
         reply = http_handle(request)
         
	 cs.send(reply)

         print("\n\nReceived request")
         print("======================")
         print(request.rstrip())
         print("======================")


         print("\n\nReplied with")
         print("======================")
         print(reply.rstrip())
         print("======================")

    return 0


def http_handle(request_string):
    
    assert not isinstance(request_string, bytes)
     
    a = request_string.split("\n")
    b = a[0].split(" ")
    reply = ""
    c= b[1].split("/")
    print c[1]
    data=""
    if b[1]=="/":
	   reply="index.html"
    else: 
	   reply = c[1]
    try:
    	    with open(reply, 'rb') as myfile:
    	    	data = myfile.read()
   	    if(reply.endswith(".html")):
		  tipo = 'text/html'
	    if(reply.endswith(".jpg")):
		  tipo = 'image/jpg'
	    if(reply.endswith(".gif")):
		  tipo = 'image/gif'
	    if(reply.endswith(".txt")):
          	tipo = 'text/txt'
	    if(reply.endswith(".py")):
          	tipo = 'text/py'
    	    headers = "HTTP/1.1 200 OK\n" + "Content-Type: "+tipo+"\n" + "Connection:close\n" + "\n"
   	    answer = "%s%s\n"%(headers, data)
   	    return answer
    except IOError:
	    with open("404.html") as mifile:
		  data =mifile.read()
	    errorA = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "Connection:close\n" + "\n"
	    answer = "%s%s\n"%(errorA, data)
	    return answer
    


if __name__ == "__main__":
    sys.exit(main())
