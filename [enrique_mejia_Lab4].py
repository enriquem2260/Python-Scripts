# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:06:51 2022

@author: enriq
"""


import time
import socket

start_time = time.time()

    
ip_address = input("Enter the ip address [127.0.0.1]:")
port_number = input("Now enter the port number you will look for: ")
    
for port_number in range(1, 1000):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_address, port_number))
    
    if (result == 0):
        print("Port " + str(port_number) +" is OPEN")
        
    else:
        print("Port " + str(port_number) +" is CLOSED")
        
    sock.close()
        
            
time.sleep()
        
        
    
