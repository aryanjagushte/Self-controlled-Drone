from djitellopy import tello
from time import sleep             #to add delays between each command

drone = tello.Tello()  # this will create our object ie drone
drone.connect()
print(drone.get_battery())   #just to check whether the drone is connected or not

drone.takeoff()   #important to make the drone fly
drone.send_rc_control(0,50,0,0)  #moving forward
sleep(2)   #2 second delay

drone.send_rc_control(-30,0,0,0)  #moving left side
sleep(2)
drone.send_rc_control(0,0,0,0)  #to stop drone moving forward, so avoid moving forward while landing
drone.land()
