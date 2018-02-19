from dronekit import connect, VehicleMode, LocationGlobalRelative
import time


def arm_and_takeoff (TargetAltitude):
#Vehicle Connection
	print ("executing takeoff")

	while not drone.is_armable:
		print ("vehicle is not armable, waiting...")
		times.sleep(1)

	print ("ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	while not drone.armed:
		print("waiting for arming...")
		time.sleep(1) 

	print("ready for takeoff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True: 
		Altitude =drone.location.global_relative_frame.alt
		print("Altitude reached")
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break



#Vehicle connection
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)
drone.airspeed = 15

A_location = LocationGlobalRelative (20.735513, -103.457498, 20)
B_location = LocationGlobalRelative (20.736369, -103.457426, 20)
C_location = LocationGlobalRelative (20.736331, -103.456801, 20)
A_location = LocationGlobalRelative (20.735513, -103.457498, 20)


drone.simple_goto(A_location)
time.sleep(30)

drone.simple_goto(B_location)
time.sleep(30)

drone.simple_goto(C_location)
time.sleep(28)

drone.simple_goto(A_location)
time.sleep(30)

#print ("baterry" volts )