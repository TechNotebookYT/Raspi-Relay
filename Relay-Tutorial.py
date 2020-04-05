import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Relay 1
GPIO.setup(21, GPIO.OUT)
# Relay 2
GPIO.setup(26, GPIO.OUT)

try:
    while True:
        GPIO.output(21, GPIO.HIGH)
        print('Relay 1 ON')
        time.sleep(1)
        GPIO.output(26, GPIO.HIGH)
        print('Relay 2 ON')
        time.sleep(1)
        GPIO.output(21, GPIO.LOW)
        print('Relay 1 OFF')
        time.sleep(1)
        GPIO.output(26, GPIO.LOW)
        print('Relay 2 OFF')
        time.sleep(1)
        
finally:
    GPIO.cleanup()
