"""
class ControllerStateTable(Object):
	def __init__(UP,LP,LR,RR,LY,RY,LT,UT,B,F):
		self.UP = 0
		self.LP= 0
		self.LR= 0
		self.RR = 0
		self.LY = 0 
		self.RY = 0
		self.LT = 0
		self.UT = 0
		self.B = 0
		self.F = 0
	def updateStateTable(structure):
		self.UP = UP
		self.LP= LP
		self.LR= LR
		self.RR = RR
`		self.LY = LY
		self.RY = RY
		self.LT = LT
		self.UT = UT
		self.B = B
		self.F = F

		


PITCH = 0
YAW = 1
ROLL = 2
BACK_FORWARD = 3
LOW_THRUST = 4
UP_THRUST = 5
#contains code mapped to the controller ouptput
#for this action
controller =
{
0:YAW
1:BACK_FORWARD
2:ROLL
3:PITCH
14:LOW_THRUST
15:UP_THRUST
}

mapp = 
{
