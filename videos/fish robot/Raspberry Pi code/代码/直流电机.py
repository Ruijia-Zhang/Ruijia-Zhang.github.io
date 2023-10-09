import RPi.GPIO as GPIO
import time

IN1 = 11
IN2 = 12
IN3 = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)

pwm = GPIO.PWM(IN1,80)
pwm.start(90)

GPIO.output(IN2,True)
GPIO.output(IN3,False)

while (True):
    pwm.ChangeDutyCycle(90)
    time.sleep(3)
    pwm.ChangeDutyCycle(30)
    time.sleep(3)
finally:
    pwm.stop()
    GPIO.cleanup()
