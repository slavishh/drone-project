from djitellopy import tello
import KeyPressModule as kp
from time import sleep


kp.init()

me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): lr = speed
    elif kp.getKey("s"): lr = -speed

    if kp.getKey("a"): ud = -speed
    elif kp.getKey("d"): ud = speed

    if kp.getKey("q"): yv = me.land(); sleep(3)
    elif kp.getKey("e"): yv = me.takeoff()

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

