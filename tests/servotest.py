import RPi.GPIO as GPIO
import time

servoPIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 als PWM mit 50Hz
p.start(2.5) # Initialisierung
try:
  while True:
    print("cycle")
    angle=float(input("enter angle"))
    p.ChangeDutyCycle(angle)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()