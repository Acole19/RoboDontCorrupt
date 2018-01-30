import setup
from setup import RPL
import post_to_web as PTW
def retrn():
    exit(0)
back_sensor = 16
left_sensor = 18
rt_sensor = 17
rt_wheel = 2
lft_wheel = 1
forward = 1000
backward = 2000
RPL.servoWrite(0,0)
command = raw_input("> ")
if command == "left":
    direction = raw_input("> ")
    if direction == "forward":
        RPL.servoWrite(lft_wheel,forward)
    elif direction == "backward":
        RPL.servoWrite(lft_wheel,backward)
elif command == "right":
    direction = raw_input("> ")
    if direction == "forward":
        RPL.servoWrite(rt_wheel,forward)
    elif direction == "backward":
        RPL.servoWrite(rt_wheel,backward)
elif command == "both":
    retrn()
else command == "stop":
    RPL.servoWrite(lft_wheel,0)
    RPL.servoWrite(rt_wheel,0)
