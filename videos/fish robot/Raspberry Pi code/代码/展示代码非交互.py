import RPi.GPIO as GPIO
import time
import serial
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# 直流电机
IN1 = 11
IN2 = 12
IN3 = 13

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)

pwm1 = GPIO.PWM(IN2,80)
pwm1.start(0)

GPIO.output(IN1,True)
GPIO.output(IN3,False)

# 转向舵机
IN4 = 15
GPIO.setup(IN4,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN4,GPIO.OUT,initial =False)
pwm2 = GPIO.PWM(IN4,50)
pwm2.start(0)
time.sleep(2)

def turnleft(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)
    pwm2.ChangeDutyCycle(0)

def turnright(p):
    pwm2.ChangeDutyCycle(p)
    time.sleep(0.2)
    pwm2.ChangeDutyCycle(0)

# 超声波
# 左
TRIG1 =16
ECHO1 = 18
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
# 右
TRIG2 =19
ECHO2 = 21
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

# 丝杠
IN5 = 22
IN6 = 23
IN7 = 24
IN8 = 26

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

# 胸鳍舵机
IN9 = 29
GPIO.setup(IN9,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN9,GPIO.OUT,initial =False)
pwm3 = GPIO.PWM(IN9,50)
pwm3.start(0)
time.sleep(2)

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

def loop1():
    dis1 = distance(TRIG1,ECHO1)
    dis2 = distance(TRIG2,ECHO2)
    global count
    if dis1>=30 and dis2<=30:
        pwm1.ChangeDutyCycle(80)
        turnleft(5.5)
        time.sleep(2)
        for i in range(1,5,1):
            turnright(5.5+i*0.5)
        pwm1.ChangeDutyCycle(100)
        count=count+1
    elif dis1<=30 and dis2>=30:
        pwm1.ChangeDutyCycle(80)
        turnright(9.5)
        time.sleep(2)
        for i in range(1,5,1):
            turnleft(9.5-i*0.5)
        pwm1.ChangeDutyCycle(100)
        count=count+1
    elif dis1<=30 and dis2<=30:
        pwm1.ChangeDutyCycle(80)
        turnright(9.5)
        time.sleep(2)
        for i in range(1,5,1):
            turnleft(9.5-i*0.5)
        pwm1.ChangeDutyCycle(100)
        count=count+1
    else:
        pwm2.ChangeDutyCycle(7.5)
        time.sleep(0.04)
        pwm2.ChangeDutyCycle(0)
    return count

def loop2(a):
    if a==1:
        for angle in range(0,30,10):
            pwm3.ChangeDutyCycle(5.5)
            forward(0.01,4)
            time.sleep(0.02)
            pwm3.ChangeDutyCycle(0)
            stop()
        print("stop turning...")
        time.sleep(4)
        for angle in range(30,0,-10):
            backward(0.01,4)
            time.sleep(0.02)
            stop()
        print("stop turning...")
        time.sleep(2)
        pwm3.ChangeDutyCycle(7.5)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
    elif a==2:
        for angle in range(0,-30,-10):
            pwm3.ChangeDutyCycle(9.4)
            backward(0.01,4)
            time.sleep(0.02)
            pwm3.ChangeDutyCycle(0)
            stop()
        print("stop turning...")
        time.sleep(4)
        for angle in range(-30,0,10):
            forward(0.01,4)
            time.sleep(0.02)
            stop()
        print("stop turning...")
        time.sleep(2)
        pwm3.ChangeDutyCycle(7.5)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
    else:
        destroy()

if __name__=='__main__':
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(0.04)
    pwm2.ChangeDutyCycle(0)
    pwm3.ChangeDutyCycle(7.5)
    time.sleep(0.04)
    pwm3.ChangeDutyCycle(0)
    while (True):
        i = 1
        print("开始")
        if i==1:
            pwm1.ChangeDutyCycle(100)
            GPIO.output(IN1,True)
            GPIO.output(IN3,False)
            count=0
            while (count<=2):
                count=loop1()
                if count==2:
                    a=1
                    if a==1:
                        print("浮")
                        time.sleep(15)
                        pwm1.ChangeDutyCycle(50)
                        loop2(1)
                        pwm1.ChangeDutyCycle(100)
                        time.sleep(2)
                        print("沉")
                        pwm1.ChangeDutyCycle(50)
                        loop2(2)
                        pwm1.ChangeDutyCycle(100)
                    else:
                        break
                else:
                    continue
        else:
            GPIO.output(IN1,False)
            pwm1.ChangDutyCycle(0)
            GPIO.output(IN3,False)
