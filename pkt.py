from scapy.all import *
#make_test(11,20,"10.0.2.15","192.168.1.6",22)

class ControlFrame(Packet):
	name="Control Frame"
	fields_desc=[ ShortField("code", 0),
		      ShortField("value",0)]
#def make_test(x, y,srcIP,dstIP,dstPort):
def make_test(x, y,srcIP,dstIP):
	#pkt = IP(src=srcIP, dst=dstIP)/TCP(dport=dstPort)/ControlFrame(code=x,value=y)
	pkt = IP(src=srcIP, dst=dstIP)/ControlFrame(code=x,value=y)
	
	pkt.show()
	send(pkt)
	

