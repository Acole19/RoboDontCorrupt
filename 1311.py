import setup
from setup import RPL
import post_to_web as PTW

def Distance():
    return RPL.readDistance(16)
def motorForw():
    RPL.servoWrite(1,2000)
    RPL.servoWrite(0,1000)

def rearreasp():
    back_sensor = 16
    rt_wheel = 0
    lft_wheel = 1
    forward = 1000
    backward = 2000
    while True:
        if Distance() < 50000:
            motorForw()
        else:
            h = 7
rearreasp()
