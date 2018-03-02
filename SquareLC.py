#***************************************************************************
# Title        : Assignment1.py
#
# Description  : This is the final code for Assingment 1
#
# Environment  : Python 2.7 Code. 
#
# License      : GNU GPL version 3
#
# Editor Used  : Sublime Text
#
# Autor		   : Luis Conrado Alcala Becerra
#
#****************************************************************************

#****************************************************************************
# Imported functions, classes and methods
#****************************************************************************
from  dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#****************************************************************************
#   Method Name     : arm_and_takeoff
#
#   Description     : Add your takeoff function from your last assignment here
#
#   Parameters      : targetAltitude
#
#   Return Value    : None
#
#****************************************************************************
def arm_and_takeoff(TargetAltitude):
	print ("Executing Takeoff")

	while not drone.is_armable:
		print ("Vehicle is not armable, waiting...")
		time.sleep(1)

	print ("Ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	while not drone.armed:
		print("Waiting for arming...")
		time.sleep(1)

	print("Ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("Altitude: %f2" % Altitude)
		time.sleep(1)
		
		if Altitude >= TargetAltitude * 0.95:
			print("Altitude has been reached")
			break

#****************************************************************************
#   Method Name     : __main__ 
#
#   Description     : This is the main thread of the python program code
#
#   Parameters      : None
#
#   Return Value    : None
#
#****************************************************************************

drone = connect('127.0.0.1:14551' , wait_ready=True)

arm_and_takeoff(15)

drone.airspeed = 4

FirstWaypoint = LocationGlobalRelative (20.736770, -103.45470, 15)
SecondWaypoint = LocationGlobalRelative (20.736745, -103.454287, 15)
ThirdWaypoint = LocationGlobalRelative (20.736443, -103.454328, 15)
FourthWaypoint = LocationGlobalRelative (20.736453, -103.454706, 15)

print("Flying to the first waypoint")
drone.simple_goto(FirstWaypoint)
time.sleep(18)

print("Flying to the second waypoint")
drone.simple_goto(SecondWaypoint)
time.sleep(18)

print("Flying to the third waypoint")
drone.simple_goto(ThirdWaypoint)
time.sleep(18)

print("Flying to Fourth Waypoint")
drone.simple_goto(FourthWaypoint)
time.sleep(18)

print ("Returning home")
drone.mode = VehicleMode("RTL")

while drone.location.global_relative_frame.alt > 1:
	print ("Landing, Alt: %f" % drone.location.global_relative_frame.alt)
	time.sleep(1)

print ("Landed!")
print ('Drone Battery: %f V' % drone.battery.voltage)

drone.close()
