#Ejemplo de cambio
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

drone = connect('udp:127.0.0.1:14551', wait_ready=True)

def arm_and_takeoff(TargetAltitude):	
	print ("Pre-arm Checks...")

	print ("Ready to arm: ", drone.is_armable)

	while not drone.is_armable:
		print("Vechile is not armable, waiting...")
		time.sleep(1)

	print("WARNING: Arming Motors!")

	drone.mode = VehicleMode("GUIDED")
	drone.armed = True

	print ("Vehicle Armed")

	while not drone.armed:
		print("Waiting for arming...")
		time.sleep(1)

	print("Taking off!")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt 

		print("Altitude: ", Altitude)

		if Altitude >= TargetAltitude * 0.95:
			print ("altitude reached")
			break

		time.sleep(1)

def LandDrone():
	print("Landing...")
	drone.mode = VehicleMode("LAND")

	while True:
		Altitude = drone.location.global_relative_frame.alt 

		print("Altitude: ", Altitude)

		if Altitude <= 0:
			print ("Landed")
			break
		time.sleep(1)

arm_and_takeoff(20)
LandDrone()
