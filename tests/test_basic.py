import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from controller.pkt import *

#Run test with sudo priveleges
class TestScapyPkttMethods(unittest.TestCase):

    def test_IP(self):
        pkt = IP(src="127.0.0.1", dst="www.google.com") / ControlFrame(code=11, value=20)
        pkt.show()
        packetList = send(pkt, return_packets=True)
        assert(packetList.__len__() == 1)

if __name__ == '__main__':
    unittest.main()