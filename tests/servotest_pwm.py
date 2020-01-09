import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  while True:
    print("cycle")
    #angle=float(input("enter angle"))
    p.ChangeDutyCycle(0)
    time.sleep(0.05)
    p.ChangeDutyCycle(1)
    time.sleep(0.01)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()