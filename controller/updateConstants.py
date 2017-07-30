import socket


def TCP_CONNECT():
    global s
    global BUFFER_SIZE
    # TCP_IP = '192.168.1.7'
    TCP_IP = '192.168.1.101'
    TCP_PORT = 5008
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))


def sendCommand(MESSAGE):
    global s
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "confirmed constants BBB:", data


TCP_CONNECT()
