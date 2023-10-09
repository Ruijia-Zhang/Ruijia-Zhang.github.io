import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

IN1 = 11
IN2 = 12
IN3 = 13

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)

pwm1 = GPIO.PWM(IN2,80)
pwm1.start(90)

GPIO.output(IN1,True)
GPIO.output(IN3,False)

IN4 = 15
GPIO.setup(IN4,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN4,GPIO.OUT,initial =False)
pwm2 = GPIO.PWM(IN4,50)
pwm2.start(7.5)
time.sleep(2)

TRIG1 =16
ECHO1 = 18
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
TRIG2 =19
ECHO2 = 21
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
TRIG3 =22
ECHO3 = 23
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)


def destroy():
    GPIO.cleanup()

def distance(name1,name2):
    GPIO.output(name1,0)
    time.sleep(0.000002)
    GPIO.output(name1,1)
    time.sleep(0.00001)
    GPIO.output(name1,0)
    while GPIO.input(name2)==0:
        pass
    emitTime = time.time()
    while GPIO.input(name2)==1:
        pass
    acceptTime = time.time()
    totalTime = acceptTime-emitTime
    distanceForReturn = totalTime*340/2*100
    return distanceForReturn

def loop():
    while (True):
        dis1 = distance(TRIG1,ECHO1)
        dis2 = distance(TRIG2,ECHO2)
        dis3 = distance(TRIG3,ECHO3)
        if dis1>=10 and dis2>=10 and dis3<=10:
            time.sleep(0.4)
            for i in range(90,123,5):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(122,89,-5):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1>=10 and dis2<=10 and dis3>=10:
            time.sleep(0.4)
            for i in range(90,57,-5):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(58,91,5):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1<=10 and dis2>=10 and dis3>=10:
            time.sleep(0.4)
            for i in range(90,57,-10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(58,91,10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1<=10 and dis2<=10 and dis3>=10:
            time.sleep(0.4)
            for i in range(90,57,-10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(58,91,10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1<=10 and dis2>=10 and dis3<=10:
            time.sleep(0.4)
            for i in range(90,123,10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(122,89,-10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1>=10 and dis2<=10 and dis3<=10:
            time.sleep(0.4)
            for i in range(90,57,-10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(58,91,10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        elif dis1<=10 and dis2<=10 and dis3<=10:
            time.sleep(0.4)
            for i in range(90,57,-10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
            for i in range(58,91,10):
                pwm1.ChangeDutyCycle(40)
                pwm2.ChangeDutyCycle(i/18+2.5)
                time.sleep(0.02)
                pwm2.ChangeDutyCycle(0)
                time.sleep(0.2)
        else:
            pwm2.ChangeDutyCycle(7.5)
            time.sleep(0.2)
            return

if __name__=='__main__':
    while (True):
        loop()
