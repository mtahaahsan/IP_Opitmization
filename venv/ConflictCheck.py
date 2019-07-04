import sys
import re
import ipaddress
import time
from IpAddress import *
from Connection import *


def main():
    # User enters host ip, username, and password
    host = input("Host: ")
    username = input("Username: ")
    password = input("Password: ")

    # Details sent to Connection class, output stored
    con = Connection(host,username,password)
    # con = Connection("94.201.11.111", "duplanning", "plann!ng@321")
    out = con.getOutput()

    # User enters the class they want to advertise, input it converted to IP Address object
    ipInput = input("Enter the IPv4 Address you'd like to advertise \n")
    ipInput = ipaddress.IPv4Network(ipInput)

    start_time = time.time()

    # Output is sent to method that returns all the IPs from the output, and marks them as used
    usedList = returnList(out, "USED")

    # Checks if the entered ip addresss is either a subnet or a supernet of another address
    if(checkSuper(usedList, ipInput)):
        if(checkSub(usedList, ipInput)):
            print("IP is free to use")

    # Outputs the used IPs to a file
    toFile(usedList, "fList.txt")
    print("Program took", round(time.time() - start_time, 2), "to run")


# Checks if user entered IP Address is a supernet of another address, returns flag
def checkSuper(ipList, ip):
    for x in ipList:
        c = True
        if(ip.subnet_of(x[0])):
            c = False
            print("There is a conflict with ", x[0], "\n")
            break
    return c

# Checks if user entered IP Address is a subnet of another address, returns flag
def checkSub(ipList, ip):
    for x in ipList:
        c = True
        if(ip.supernet_of(x[0])):
            c = False
            print(ip, " is a supernet of ", x[0], "\n")
            break
    return  c

# Writes a list to a file (Can be modifyed for user input)
def toFile(allList, file):
    f = open(file, "w+")
    for x in allList:
        f.write(x[0].__str__())
        f.write("\n")
    f.close()

# Takes the output from the Connection class and finds all the IP Addresses inside the output
def returnList(input, type):
    # f = open(file, "r")

    # contents = f.read()
    func = lambda x:ipaddress.IPv4Network(x)
    myList = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\/(?:[\d]{1,3})', input)

    # Converts all the found IP addresses (str) into IP Address objects
    myList = [(ipaddress.IPv4Network(x), type) for x in myList]
    myList.sort()

    # Removes duplicates IPs
    myList = list(dict.fromkeys(myList))

    return myList

main()