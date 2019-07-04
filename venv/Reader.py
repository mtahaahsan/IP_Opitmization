import sys
import re
import ipaddress
import time
import netmiko
from netmiko import ConnectHandler
from IpAddress import *

def main():
    start_time = time.time()
    # Opens file and reads all contentes
    f = open("Speedtest_Don.txt", "r")
    contents = f.read()

    sub9List = []

    # Finds all IPs starting from 31, finds all possible supernets of 30 from those 31, and then finds all 30 and merges
    # with the supernets of 30, then finds all 29 supernets, and so on until it subnet 9
    sub31List = findAllIP(contents, 31)
    # print(sub31List, "\n")
    sub30List = findSuper(sub31List)

    sub30List = process(sub30List, 30, contents)
    sub29List = findSuper(sub30List)

    # Gets all /29 addresses from text file, adds them to list that contains the supermasks of 30
    sub29List = process(sub29List, 29, contents)
    sub28List = findSuper(sub29List)

    sub28List = process(sub28List, 28, contents)
    sub27List = findSuper(sub28List)

    sub27List = process(sub27List, 27, contents)
    sub26List = findSuper(sub27List)

    sub26List = process(sub26List, 26, contents)
    sub25List = findSuper(sub26List)

    sub25List = process(sub25List, 25, contents)
    sub24List = findSuper(sub25List)

    sub24List = process(sub24List, 24, contents)
    sub23List = findSuper(sub24List)

    sub23List = process(sub23List, 23, contents)
    sub22List = findSuper(sub23List)

    sub22List = process(sub22List, 22, contents)
    sub21List = findSuper(sub22List)

    sub21List = process(sub21List, 21, contents)
    sub20List = findSuper(sub21List)

    sub20List = process(sub20List, 20, contents)
    sub19List = findSuper(sub20List)

    sub19List = process(sub19List, 19, contents)
    sub18List = findSuper(sub19List)

    sub18List = process(sub18List, 18, contents)
    sub17List = findSuper(sub18List)

    sub17List = process(sub17List, 17, contents)
    sub16List = findSuper(sub17List)

    sub16List = process(sub16List, 16, contents)
    sub15List = findSuper(sub16List)

    sub15List = process(sub15List, 15, contents)
    sub14List = findSuper(sub15List)

    sub14List = process(sub14List, 14, contents)
    sub13List = findSuper(sub14List)

    sub13List = process(sub13List,13, contents)
    sub12List = findSuper(sub13List)

    sub12List = process(sub12List, 12, contents)
    sub11List = findSuper(sub12List)

    sub11 = process(sub11List, 11, contents)
    sub10List = findSuper(sub11List)

    sub10List = process(sub10List, 10, contents)
    sub9List = findSuper(sub10List)

    sub9List = process(sub9List, 9, contents)



    SuperList = [sub31List, sub30List, sub29List, sub28List, sub27List, sub26List, sub25List, sub24List, sub23List,
                 sub22List, sub21List, sub20List, sub19List, sub18List, sub17List, sub16List, sub15List, sub14List,
                 sub13List, sub12List, sub11List, sub10List, sub9List]


    print("My program took", round(time.time() - start_time, 2), "to run")

    # Allows user to choose which subnet to display from the list of all ip addresses
    userInput(SuperList)

# Takes a list of IP addresses (str) and converts them to IP Address Objects
def convert(ipList):
    ipList = [ipaddress.IPv4Network(x) for x in ipList]
    ipList.sort()
    ipList = list(dict.fromkeys(ipList))
    # print(regex)
    return ipList

# Takes a sorted list of IPs, compares two ip's to see if they're in the same super class
# if they are, then add the supernet to a separate list, returns list in the en
def findSuper(ipList):
    y = 1
    subList = []
    while y <= ipList.__len__() - 1:
        if ((ipList[y - 1].supernet() == ipList[y].supernet())):
            subList.append(ipList[y - 1].supernet())
            # ipList[y] = 0
            # ipList[y-1] = 0
            del ipList[y]
            del ipList[y-1]
        else:
            y = y + 1
    return subList

# takes an the file contents, a submask, and finds all the instances of that subnet in the file contents
def findAllIP(contents, submask):
    regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\/' + submask.__str__(), contents)
    regex = convert(regex)
    return regex

# Pritns the user requested submasks from to a file
def toTextFile(textFile, superList, submask):
    f = open(textFile, "w+")
    if (submask != "all"):
        tot = 32 - int(submask) - 1
        print("/",submask, " Addresses", end="")
        for x in superList[tot]:
            f.write(str(x))
            f.write("\n")
        f.close()
    else:
        for eachList in superList:
            for y in eachList:
                f.write(str(y))
                f.write("\n")

    f.close()

def removeNone(myList):
    return[x for x in myList if x != 0]

def removeDuplicates(myList):
    myList = list(dict.fromkeys(myList))
    return myList

# Process method to remove repitiion
def process(myList, submask, contents):
    myList.extend(findAllIP(contents, submask))
    # myList.sort()
    myList = removeDuplicates(myList)
    # print(myList, "\n")
    return myList

# User chooses which submask they're looking for, and which file to write to
def userInput(superList):
    userInput = input("Which submask are you looking for?\n")
    userFile = input("Please name the file with the extension\n")
    print("Displaying all /", userInput, " submarks", sep="")
    toTextFile(userFile, superList, userInput)

main()

