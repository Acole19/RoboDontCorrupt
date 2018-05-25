import setup
from setup import RPL
import post_to_web as PTW
import time
left_sensor = 16
rear = 17
rt_wheel = 0
lft_wheel = 1
forward = 1000
backward = 2000
condit = 7
x = 0
while condit != 18:
    RPL.servoWrite(1,2000)
    RPL.servoWrite(2,1000)
    if x > 10:
        z = 3
        while z == 3:
            if RPL.readDistance(rear) < 1000:
                RPL.servoWrite(2,0)
                RPL.servoWrite(1,0)
                z = 5
            if RPL.readDistance(rear) > 40000:
                RPL.servoWrite(1,1500)
                RPL.servoWrite(2,500)
            if RPL.readDistance(rear) > 70000:
                RPL.servoWrite(1,2500)
                RPL.servoWrite(2,1499)
            if RPL.readDistance(rear) < 1000:
                RPL.servoWrite(2,0)
                RPL.servoWrite(1,0)
                z = 5
                condit = 18
    if RPL.readDistance(16) > 50000:
        RPL.servoWrite(1,000)
        RPL.servoWrite(2,1000)
        time.sleep(.5)
        x += 1
    if RPL.readDistance(16) < 10000:
        RPL.servoWrite(1,2000)
        RPL.servoWrite(2,000)
        time.sleep(.5)
        x += 1
    if RPL.readDistance(16) > 10000 and RPL.readDistance(16) < 50000:
        x += 1
    else:
        x += 1
    RPL.servoWrite(1,2000)
    RPL.servoWrite(2,1000)
