import time
import RPi.GPIO as GPIO
import os, subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)

try:
	while True:
		stick = GPIO.input(7)
		if (stick == 0):
			time.sleep(0.5)
			print "Capturing a proto...";
			p = subprocess.Popen('/home/pi/RPICamTX/icap')
			p.wait()
		else:
			time.sleep(0.5)
			print "Standby...";

except KeyboardInterrupt:
		GPIO.cleanup()
