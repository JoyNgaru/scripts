#!/usr/bin/python3

import os
def update():
    
    pg = input("We are updating the system   : ")
    os.system("sudo yum update; sudo yum upgrade " + pg + " -y")
 
update()
