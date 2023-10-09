import RPi.GPIO as GPIO
import time
#步进角7.5
IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

def setStep(w1,w2,w3,w4):
    GPIO.output(IN1,w1)
    GPIO.output(IN2,w2)
    GPIO.output(IN3,w3)
    GPIO.output(IN4,w4)

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

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)

def destroy():
        GPIO.cleanup()

def loop():
    while True:
        i = int(input("1、正转\t2、反转\t3、退出\n请输入数字:"))
        if i==1:
            b = int(input("请输入圈数:"))
            forward(0.01,48*b)
            print("请等待3秒...")
            time.sleep(3)
            print("stop...")
            stop()
        elif i==2:
            a = int(input("请输入圈:"))
            backward(0.01,48*a)
            print("请等待3秒...")
            time.sleep(3)
            print("stop...")
            stop()
        else:
            destroy()
            return


if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
