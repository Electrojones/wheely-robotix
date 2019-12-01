import RPi.GPIO as GPIO
import time

#where the servos are attached
servopins=[17, 27, 22]

#servos as object
servos=[]

#init pins
GPIO.setmode(GPIO.BCM)
for pin in servopins:
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(8.8)
    servos.append(p)

#give an array of 3 values to this function to adjust the angles of the servos
def set_servos(angles):

    #do it for each servo/angle
    for servo, angle in zip(servos, angles):
        #set boundaries for values
        if angle > 14:
            angle=14
        if angle < 2:
            angle=2
        print(angle)
        #set the values
        servo.ChangeDutyCycle(angle)
        time.sleep(0.5)

#give an array of servo-values-sets
def set_servos_array(angle_set_array):
    pass

def end():
    p.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    set_servos([14, 14, 1])
    end()