import time

import atexit

import string

import socket, traceback

import math





while 1:
 host="192.168.102.51"

 port=5555

 s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

 s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

 s.bind((host, port))


 message, address = s.recvfrom(8192)

 

 var1 = message

 var2=var1.split(',')

 temp2=var2[8].strip(',')

 print()

