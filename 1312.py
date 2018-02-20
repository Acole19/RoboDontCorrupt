import time
import setup
from setup import RPL
z = time.time()









while True:
    y = time.time() - z
    if y % 4 == 0:
        RPL.servoWrite(1,2000)
        RPL.servoWrite(0,1000)
    if y % 8 == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(0,0)
RPL.servoWrite(0,0)
RPL.servoWrite(1,0)
