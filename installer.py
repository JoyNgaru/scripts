#!/usr/bin/python3
 
import os
 
def inst():
    pg = input("What program would you like to install: ")
    os.system("sudo yum install " + pg + " -y")
 
inst()
