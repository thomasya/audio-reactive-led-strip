import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

rLED = GPIO.PWM(15, 2000)
rLED.start(0)
try:
	while 1:
		for dc in range (0,101,1):
			rLED.ChangeDutyCycle(dc)
			time.sleep(0.1)
except KeyboardInterrupt:
	pass
rLED.stop()
GPIO.cleanup
