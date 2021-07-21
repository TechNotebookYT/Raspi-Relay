from gpiozero import LED
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
pir = MotionSensor(17) # PIR Motion Sensor


# Relay 1
GPIO.setup(21, GPIO.OUT)
# Relay 2
# GPIO.setup(26, GPIO.OUT)

try:
    while True:
        pir.wait_for_motion()
        print("Motion Detected")
        GPIO.output(21, GPIO.HIGH)
        print('Relay 1 ON')
        # time.sleep(7)
	#pir.wait_for_no_motion()
	pir.wait_for_no_motion()
	time.sleep(7)
	GPIO.output(21, GPIO.LOW)
	print('Relay 1 OFF')
	# GPIO.output(26, GPIO.HIGH)
        # print('Relay 2 ON')
        # time.sleep(1)
        ### GPIO.output(21, GPIO.LOW)
        ### print('Relay 1 OFF')
        # time.sleep(1)
        # GPIO.output(26, GPIO.LOW)
        # print('Relay 2 OFF')
        # time.sleep(1)
        
finally:
     GPIO.cleanup()
    # GPIO.output(21, GPIO.HIGH)
    
    



 
# RELAIS_1_GPIO = 21
# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
# GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
# GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on


# led = LED(21)

# led.off()

# while True:
       
        # GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
        # time.sleep(2)
        # pir.wait_for_motion()
        # GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
        # print("Motion Stopped")
        # time.sleep(2)


#This was added on a new branch called july2021
