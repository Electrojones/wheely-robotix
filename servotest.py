import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)

p = GPIO.PWM(0, 50)

p.start(2.5)