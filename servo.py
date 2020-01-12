import RPi.GPIO as GPIO
import time

#where the servos are attached
servopins=[15, 11, 16, 13, 18, 22]

#servos as object
servos=[]

#init pins
GPIO.setmode(GPIO.BOARD)
for pin in servopins:
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 50)
    p.start(7)
    servos.append(p)
    time.sleep(0.3)

#give an array of 3 values to this function to adjust the angles of the servos
def set_servos(angles):

    #do it for each servo/angle
    for servo, angle in zip(servos, angles):
        #set boundaries for values
        if angle > 11:
            angle=11
        if angle < 3:
            angle=3
        
        time.sleep(0.3)

        #set the values
        servo.ChangeDutyCycle(angle)

#give an array of servo-values-sets
def set_servos_array(angle_set_array, wait_time):
    for angles in angle_set_array:
        set_servos(angles)
        time.sleep(wait_time)   

def pause():
    for servo in servos:
        servo.ChangeDutyCycle(0)

def end():
    p.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    set_servos([14, 14, 1])
    end()