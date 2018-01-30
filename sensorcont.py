import setup
from setup import RPL
import post_to_web as PTW
def retrn():
    exit(0)
def usercont():
    back_sensor = 16
    left_sensor = 18
    rt_sensor = 17
    rt_wheel = 0
    lft_wheel = 1
    forward = 1000
    backward = 2000
    RPL.servoWrite(0,0)
    command = raw_input("> ")
    if command == "left":
        direction = raw_input("> ")
        if direction == "backward":
            RPL.servoWrite(lft_wheel,forward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
        elif direction == "forward":
            RPL.servoWrite(lft_wheel,backward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
    elif command == "right":
        direction = raw_input("> ")
        if direction == "backward":
            RPL.servoWrite(rt_wheel,forward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
        elif direction == "forward":
            RPL.servoWrite(rt_wheel,backward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
    elif command == "both":
        direction = raw_input("> ")
        if direction == "backward":
            RPL.servoWrite(lft_wheel,backward)
            RPL.servoWrite(rt_wheel,forward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
        elif direction == "forward":
            RPL.servoWrite(rt_wheel,backward)
            RPL.servoWrite(lft_wheel,forward)
            followup = raw_input("> ")
            if followup == "stop":
                RPL.servoWrite(lft_wheel,0)
                RPL.servoWrite(rt_wheel,0)
                retrn()
    elif command == "stop":
        RPL.servoWrite(lft_wheel,0)
        RPL.servoWrite(rt_wheel,0)
    else:
        RPL.servoWrite(lft_wheel,0)
        RPL.servoWrite(rt_wheel,0)

usercont()
