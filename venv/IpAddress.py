class IpAddress:
    def __init__(self, ip, flag):
        self.ip = ip
        self.flag = flag


    def printData (self):
        print(self.ip)
        print(self.flag)

    def getIP(self):
        return self.ip

    def getFlag(self):
        return self.ip


def main():
    op = IpAddress("192.168.1.0/24", "TRUE")
    print(op.getFlag())
