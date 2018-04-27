import setup
from setup import RPL
import post_to_web as PTW

def Distance():
    return RPL.readDistance(16)
def motorForw():
    RPL.servoWrite(1,2000)
    RPL.servoWrite(2,1000)
def motorstop():
    RPL.servoWrite(1,000)
    RPL.servoWrite(2,000)
def motorLeft():
    RPL.servoWrite(1,000)
    RPL.servoWrite(2,1000)
def motorRight():
    RPL.servoWrite(1,1000)
    RPL.servoWrite(2,000)
back_sensor = 16
rt_wheel = 0
lft_wheel = 1
forward = 1000
backward = 2000
condit = 7
while condit != 16:
    motorForw()
    Distance()
    if Distance() < 50000 and Distance() > 10000:
        motorForw()
    elif Distance() > 50000:
        motorLeft()
    elif Distance() > 10000:
        motorRight
    
    if RPL.readDistance(17) < 1000:
        condit = 16
motorstop()
