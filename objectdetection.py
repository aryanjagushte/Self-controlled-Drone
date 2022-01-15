from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()    #it will give the frames

while True:
    img = drone.get_frame_read().frame  #it will give individual image from drone

    img = cv2.resize(img,(360,240))  #resizing image to smaller size to get it faster

    cv2.imshow("Image",img)
    cv2.waitKey(1)

    pass
