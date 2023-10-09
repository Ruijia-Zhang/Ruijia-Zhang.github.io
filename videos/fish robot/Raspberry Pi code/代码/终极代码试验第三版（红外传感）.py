import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#推进电机
IN1 = 11
IN2 = 12
IN3 = 13

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)

pwm1 = GPIO.PWM(IN2,80)
pwm1.start(100)

GPIO.output(IN1,True)
GPIO.output(IN3,False)

#舵机
IN4 = 15
GPIO.setup(IN4,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN4,GPIO.OUT,initial =False)
pwm2 = GPIO.PWM(IN4,50)
pwm2.start(7.5)
time.sleep(2)

def turnleft(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)

def turnright(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)

#红外传感
GPIO_OUT1 = 16#前
GPIO_OUT2 =18#右
GPIO_OUT3 =19#左
GPIO.setup(GPIO_OUT1,GPIO.IN)
GPIO.setup(GPIO_OUT2,GPIO.IN)
GPIO.setup(GPIO_OUT3,GPIO.IN)

#丝杠
IN5 = 21
IN6 = 22
IN7 = 23
IN8 = 24

GPIO.setup(IN5,GPIO.OUT)
GPIO.setup(IN6,GPIO.OUT)
GPIO.setup(IN7,GPIO.OUT)
GPIO.setup(IN8,GPIO.OUT)

def setStep(w1,w2,w3,w4):
    GPIO.output(IN5,w1)
    GPIO.output(IN6,w2)
    GPIO.output(IN7,w3)
    GPIO.output(IN8,w4)

def stop():
    setStep(0,0,0,0)

def forward(delay,steps):
    for i in range(0,steps):
        setStep(1,0,1,0)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(1,0,0,1)
        time.sleep(delay)

def backward(delay,steps):
    for i in range(0,steps):
        setStep(1,0,0,1)
        time.sleep(delay)
        setStep(0,1,0,1)
        time.sleep(delay)
        setStep(0,1,1,0)
        time.sleep(delay)
        setStep(1,0,1,0,)
        time.sleep(delay)

def destroy():
    GPIO.cleanup()

angle = 0

def loop1(a):
    if a==0:
        for angle in range(0,30,10):
            forward(0.01,4)
            time.sleep(0.02)
            stop()
    elif a==1:
        for angle in range(0,-30,-10):
            backward(0.01,4)
            time.sleep(0.02)
            stop()
    else:
        destroy()

def loop2():
    count = 0
    b = random.randint(0,9)
    while (True):
        if count>=0 and count<b:
            if GPIO.input(GPIO_OUT1)==True and GPIO.input(GPIO_OUT2)==True and GPIO.input(GPIO_OUT3)==0:
                turnright(9.4)
                time.sleep(2)
                turnleft(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==True and GPIO.input(GPIO_OUT2)==0 and GPIO.input(GPIO_OUT3)==True:
                turnleft(5.5)
                time.sleep(2)
                turnright(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==0 and GPIO.input(GPIO_OUT2)==True and GPIO.input(GPIO_OUT3)==True:
                turnleft(5.5)
                time.sleep(2)
                turnright(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==0 and GPIO.input(GPIO_OUT2)==0 and GPIO.input(GPIO_OUT3)==True:
                turnleft(5.5)
                time.sleep(2)
                turnright(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==0 and GPIO.input(GPIO_OUT2)==True and GPIO.input(GPIO_OUT3)==0:
                turnright(9.4)
                time.sleep(2)
                turnleft(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==True and GPIO.input(GPIO_OUT2)==0 and GPIO.input(GPIO_OUT3)==0:
                turnleft(5.5)
                time.sleep(2)
                turnright(7.5)
                time.sleep(1)
                count=count+1
            elif GPIO.input(GPIO_OUT1)==0 and GPIO.input(GPIO_OUT2)==0 and GPIO.input(GPIO_OUT3)==0:
                turnleft(5.5)
                time.sleep(2)
                turnright(7.5)
                time.sleep(1)
                count=count+1
            else:
                if count>0:
                    count=count-1
                    continue
                else:
                    continue
        else:
            break
    time.sleep(2)
    pwm2.ChangeDutyCycle(7.5)
    return b

if __name__=="__main__":
    while (True):
        loop2()
        b = loop2()
        time.sleep(5)
        loop1(b%2)
        time.sleep(4)
        loop1((b-1)%2)
