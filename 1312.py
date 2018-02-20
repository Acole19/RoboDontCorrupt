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
    if div3() == 0 and div5() == 0:
        RPL.servoWrite(1,1000)
        RPL.servoWrite(0,2000)
    elif div3() == 0 and div5() != 0:
        RPL.servoWrite(1,2000)
    elif div3() != 0 and div5 == 0:
        RPL.servoWrite(0,1000)
RPL.servoWrite(0,0)
RPL.servoWrite(1,0)
