import sys
import re
import ipaddress


def main():
    f = open("All Private IPs.txt", "r")
    number = 31
    contents = f.read()
    sub31List = []
    sub30List = []
    sub29List = []
    sub28List = []
    sub27List = []
    sub26List = []
    sub25List = []
    sub24List = []
    sub23List = []
    sub22List = []
    sub21List = []
    sub20List = []
    sub19List = []
    sub18List = []
    sub17List = []

    regex = findAllIP(contents, 31)
    sub31List = regex
    sub30List = findSuper(regex)
    print(regex, "\n")

    regex = findAllIP(contents, 30)
    sub30List.extend(regex)
    print(sub30List, "\n")
    sub29List = findSuper(sub30List)

    # Gets all /29 addresses from text file, adds them to list that contains the supermasks of 30
    regex = findAllIP(contents, 29)
    sub29List.extend(regex)
    print(sub29List, "\n")
    sub28List = findSuper(sub29List)

    regex = findAllIP(contents, 28)
    sub28List.extend(regex)
    print(sub28List, "\n")
    sub27List = findSuper(sub28List)

    regex = findAllIP(contents, 27)
    sub27List.extend(regex)
    print(sub27List, "\n")
    sub26List = findSuper(sub27List)

    regex = findAllIP(contents, 26)
    sub26List.extend(regex)
    print(sub26List, "\n")
    sub25List = findSuper(sub26List)

    regex = findAllIP(contents, 25)
    sub25List.extend(regex)
    print(sub25List, "\n")
    sub24List = findSuper(sub25List)

    regex = findAllIP(contents, 24)
    sub24List.extend(regex)
    print(sub24List, "\n")
    sub23List = findSuper(sub24List)

    regex = findAllIP(contents, 23)
    sub23List.extend(regex)
    print(sub23List, "\n")
    sub22List = findSuper(sub23List)

    regex = findAllIP(contents, 22)
    sub22List.extend(regex)
    print(sub22List, "\n")
    sub21List = findSuper(sub22List)

    regex = findAllIP(contents, 21)
    sub21List.extend(regex)
    print(sub21List, "\n")

    SuperList = [sub31List, sub30List, sub29List, sub28List, sub27List, sub26List, sub25List, sub24List, sub23List,
                 sub22List, sub21List]
    toTextFile("sometext.txt", SuperList)
    # regex = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\/13', contents)
    # print(regex)


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
            y = y + 2
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


main()

# for x in range(regex.__len__()-1):
#     # print(x)
#     current = ipaddress.IPv4Interface(regex[x])
#     smallest = None
#
#     for y in range(x+1, regex.__len__()-1):
#         if(ipaddress.IPv4Interface(regex[y]) < current):
#             smallest = ipaddress.IPv4Interface(regex[y])
#     temp = smallest
#     smallest = regex[x]
#     regex[x] = temp
