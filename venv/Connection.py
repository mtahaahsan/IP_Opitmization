import getpass
import sys
import telnetlib

# Used to store information about the connection to make
class Connection():
    def __init__(self, myHost, myUsername, myPassword):
        self.host = myHost
        self.user = myUsername
        self.password = myPassword

    # Returns host
    def getHost(self):
        return self.host

    # Returns username
    def getUser(self):
        return self.user

    # Returns password
    def getPassword(self):
        return self.password

    # Establishes the connection, runs a "show ip route" command, returns the output
    def getOutput(self):
        HOST = self.getHost()
        password = self.getPassword()
        user = self.getUser()

        tn = telnetlib.Telnet(HOST)

        tn.read_until(b"Username: ")
        tn.write((user + "\n").encode('ascii'))
        if password:
            tn.read_until(b"Password: ")
            tn.write((password + "\n").encode('ascii'))

        tn.write(b"  show ip route\n\r")
        tn.write(b"  quit\n\r")
        output = tn.read_until(b"quit",5).decode('ascii')
        # print(output)

        return output