import setup
from setup import RPL
import post_to_web as PTW
import time
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
    RPL.servoWrite(1,2000)
    RPL.servoWrite(2,000)
left_sensor = 16
rear = 17
rt_wheel = 0
lft_wheel = 1
forward = 1000
backward = 2000
condit = 7
x = 0
while condit != 16:
    motorForw()
    if x > 10:
        while z == 3:
            if RPL.readDistance(rear) < 1000:
                RPL.servoWrite(0,0)
                RPL.servoWrite(1,0)
                z = 5
            if RPL.readDistance(rear) > 40000:
                RPL.servoWrite(1,1500)
                RPL.servoWrite(0,500)
            if RPL.readDistance(rear) > 70000:
                RPL.servoWrite(1,2500)
                RPL.servoWrite(0,1499)
            if RPL.readDistance(rear) < 1000:
                RPL.servoWrite(0,0)
                RPL.servoWrite(1,0)
                z = 5
    if RPL.readDistance(17) < 1000:
        condit = 16
    if Distance() > 50000:
        motorLeft()
        time.sleep(.5)
        x += 1
    elif Distance() < 10000:
        motorRight()
        time.sleep(.5)
        x += 1
    else:
        x += 1
    motorForw()


motorstop()
