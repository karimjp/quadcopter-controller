from scapy.all import *


class ControlFrame(Packet):
    name = "Control Frame"
    fields_desc = [ShortField("code", 0),
                   ShortField("value", 0)]