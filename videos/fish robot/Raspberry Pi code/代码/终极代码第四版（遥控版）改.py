import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#推进电机
IN1 = 11
IN2 = 12
IN3 = 13

GPIO.setup(IN1,GPIO.OUT,initial=False)
GPIO.setup(IN2,GPIO.OUT,initial=False)
GPIO.setup(IN3,GPIO.OUT,initial=False)

pwm1 = GPIO.PWM(IN2,80)
pwm1.start(0)

#舵机
IN4 = 15
GPIO.setup(IN4,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN4,GPIO.OUT,initial=False)
pwm2 = GPIO.PWM(IN4,50)
pwm2.start(7.5)
time.sleep(2)

def turnleft(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)

def turnright(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)

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
    if a==3:
        for angle in range(0,30,10):
            forward(0.01,4)
            time.sleep(0.02)
            stop()
    elif a==4:
        for angle in range(0,-30,-10):
            backward(0.01,4)
            time.sleep(0.02)
            stop()
    else:
        destroy()

def loop2(b):
    if b==1:
        turnright(9.4)
        time.sleep(2)
        turnleft(7.5)
    elif b==2:
        turnleft(5.5)
        time.sleep(2)
        turnright(7.5)
    else:
        destroy()

if __name__=="__main__":
    while (True):
        i = 0
        i = int(input("请输入1开始运动"))
        if i==1:
            pwm1.ChangeDutyCycle(100)
            GPIO.output(IN1,True)
            GPIO.output(IN3,False)
            while (True):
                a = int(input("输入1，右转，输入2，左转，输入3，上浮，输入4，下沉："))
                if a==1 or a==2:
                    pwm1.ChangeDutyCycle(50)
                    loop2(a)
                    pwm1.ChangeDutyCycle(100)
                elif a==3 or a==4:
                    pwm1.ChangeDutyCycle(50)
                    loop1(a)
                    pwm1.ChangeDutyCycle(100)
                else:
                    break
        else:
            GPIO.output(IN1,False)
            pwm1.ChangeDutyCycle(0)
            GPIO.output(IN3,False)
