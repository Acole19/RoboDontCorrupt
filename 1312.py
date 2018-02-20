import time
import setup
from setup import RPL
z = time.time()
def div3():
    y = z - time.time()
    h = y % 3
    return h
def div5():
    y = z - time.time()
    g = y % 5
    return g

while True:
    y = z - time.time()
    if y % 4 == 0:
        RPL.servoWrite(1,2000)
        RPL.servoWrite(0,1000)
    elif y % 8 == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)
RPL.servoWrite(0,0)
RPL.servoWrite(1,0)
