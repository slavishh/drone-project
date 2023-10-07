from djitellopy import tello
import KeyPressModule as kp
from time import sleep
import cv2

kp.init()
me = tello.Tello
me.connect()
print(me.get_battery())

me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): lr = speed
    elif kp.getKey("DOWN"): lr = -speed

    if kp.getKey("w"): lr = speed
    elif kp.getKey("s"): lr = -speed

    if kp.getKey("a"): lr = -speed
    elif kp.getKey("d"): lr = speed

    if kp.getKey("q"): yv = me.land(); sleep(3)
    elif kp.getKey("e"): yv = me.takeoff()

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image, img")
    cv2.waitKey(1)
