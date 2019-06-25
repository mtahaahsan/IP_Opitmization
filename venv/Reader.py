import sys
import re
import ipaddress
import time

def main():
    start_time = time.time()
    f = open("All Private IPs.txt", "r")
    number = 31
    contents = f.read()


    sub31List = findAllIP(contents, 31)
    print(sub31List, "\n")
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
    toTextFile("sometext.txt", SuperList)
    print("My program took", time.time() - start_time, "to run")


def convert(ipList):
    for x in range(ipList.__len__()):
        ipList[x] = ipaddress.IPv4Network(ipList[x])
    ipList.sort()
    ipList = list(dict.fromkeys(ipList))
    # print(regex)
    return ipList


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


def findAllIP(contents, submask):
    regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\/' + submask.__str__(), contents)
    regex = convert(regex)
    return regex

def toTextFile(textFile, superList):
    f = open(textFile, "w+")
    tot = 32
    for ipList in superList:
        tot -= 1
        f.write("/")
        f.write(tot.__str__())
        f.write(" Addresses\n")
        for x in range(ipList.__len__()):
            f.write(ipList[x].__str__())
            f.write("\n")
        f.write("\n")
    f.close()

def removeNone(myList):
    return[x for x in myList if x != 0]

def removeDuplicates(myList):
    myList = list(dict.fromkeys(myList))
    return myList

def process(myList, submask, contents):
    myList.extend(findAllIP(contents, submask))
    myList.sort()
    myList = removeDuplicates(myList)
    print(myList, "\n")
    return myList


main()

