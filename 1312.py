import time
import setup
from setup import RPL
def div3():
    return time.time() % 3
def div5():
    return time.time() % 5

while True:
    if div3() == 0 and div5() == 0:
      RPL.servoWrite(1,1000)
      RPL.servoWrite(0,2000)
  elif div3() == 0 and div5() != 0:
      RPL.servoWrite(1,2000)
  elif div3() != 0 and div5 == 0:
      RPL.servoWrite(0,1000)
  else:
      RPL.servoWrite(0,0)
      RPL.servoWrite(1,0)
