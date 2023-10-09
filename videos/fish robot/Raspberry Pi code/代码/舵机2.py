import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup)

IN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(IN,GPIO.OUT,initial = False)
pwm = GPIO.PWM(IN,50)
pwm.start(0)
time.sleep(2)

while (True):
    for i in range(90,-1,10):
        pwm.ChangeDutyCycle(i/18+2.5)
        time.sleep(0.02)
        pwm.ChangeDutyCycle(0)
        time.sleep(0.2)
    for i in range(0,91,-10):
        pwm.ChangeDutyCycle(i/18+2.5)
        time.sleep(0.02)
        pwm.ChangeDutyCycle(0)
        time.sleep(0.2)

GPIO.cleanup()
