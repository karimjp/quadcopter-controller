#!/usr/bin/env python

import subprocess
import socket

# import dbg

codeFilterList = [4, 5, 6]
codeValidList = [0, 2, 3, 14, 15, 28, 27]


# code 28 = X button -> shutdown
def runProcess(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while (True):
        retcode = p.poll()  # returns None while subprocess is running
        line = p.stdout.readline()
        yield line
        if (retcode is not None):
            break


def filterOutInput(fields):
    field2 = fields[2].split(" ")
    # if int(field2[2]) not in codeFilterList:
    if int(field2[2]) in codeValidList:
        return True
    return False


def TCP_CONNECT():
    global s
    global BUFFER_SIZE
    # TCP_IP = '192.168.1.7'
    TCP_IP = '192.168.1.101'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))


def sendCommand(code, value):
    global s
    MESSAGE = cleanInput(code, value)
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "confirmed received data by BBB:", data


# s.close()

def cleanInput(code, value):
    c_startIndex = 3 + 2
    c_endIndex = code.find("(")
    code = code[c_startIndex:c_endIndex]
    v_startIndex = 4 + 2
    value = value[v_startIndex:]
    # print code + "|" + value
    return code + '|' + value


def main():
    TCP_CONNECT()
    for line in runProcess(["evtest", "/dev/input/event6"]):
        fields = line.split(',')
        if len(fields) > 2:
            if filterOutInput(fields):
                # print fields[2], fields[3]
                code = fields[2]
                value = fields[3]
                sendCommand(code, value)


if __name__ == "__main__":
    main()
