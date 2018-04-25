import time
import setup
from setup import RPL
z = time.clock()
while True:
    y = time.clock() - z
    if y % 2 == 0:
        RPL.servoWrite(1,2000)
        RPL.servoWrite(0,1000)
    if y % 4 == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)
RPL.servoWrite(0,0)
RPL.servoWrite(1,0)
