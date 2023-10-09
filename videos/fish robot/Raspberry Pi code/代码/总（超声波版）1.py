import serial
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#直流电机
IN1 = 11
IN2 = 12
IN3 = 13
GPIO.setwarnings(False)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)

pwm1 = GPIO.PWM(IN2,80)
pwm1.start(90)

GPIO.output(IN1,True)
GPIO.output(IN3,False)
#陀螺仪
AngleData = [0.0] * 8
FrameState = 0  # 通过0x后面的值判断属于哪一种情况
Bytenum = 0  # 读取到这一段的第几位
CheckSum = 0  # 求和校验位
Angle = [0.0] * 3
#舵机
IN4 = 15
GPIO.setup(IN4,GPIO.OUT)

GPIO.setwarnings(False)
GPIO.setup(IN4,GPIO.OUT,initial =False)
pwm2 = GPIO.PWM(IN4,50)
pwm2.start(7.5)
time.sleep(2)
#超声波
TRIG1 =16
ECHO1 = 18
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
TRIG2 =19
ECHO2 = 21
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
#丝杠步进电机
#步进角7.5
IN5 = 22
IN6 = 23
IN7 = 24
IN8 = 26

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

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN5,GPIO.OUT)
    GPIO.setup(IN6,GPIO.OUT)
    GPIO.setup(IN7,GPIO.OUT)
    GPIO.setup(IN8,GPIO.OUT)
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
def destroy():
        GPIO.cleanup()
def DueData(inputdata):  # 新增的核心程序，对读取的数据进行划分，各自读到对应的数组里
    global FrameState  # 在局部修改全局变量，要进行global的定义
    global Bytenum
    global CheckSum
    global Angle
    for data in inputdata:  # 在输入的数据进行遍历
        # Python2软件版本这里需要插入 data = ord(data)*****************************************************************************************************
        if FrameState == 0:  # 当未确定状态的时候，进入以下判断
            if data == 0x55 and Bytenum == 0:  # 0x55位于第一位时候，开始读取数据，增大bytenum
                CheckSum = data
                Bytenum = 1
                continue
            elif data == 0x51 and Bytenum == 1:  # 在byte不为0 且 识别到 0x51 的时候，改变frame
                CheckSum += data
                FrameState = 1
                Bytenum = 2
            elif data == 0x52 and Bytenum == 1:  # 同理
                CheckSum += data
                FrameState = 2
                Bytenum = 2
            elif data == 0x53 and Bytenum == 1:
                CheckSum += data
                FrameState = 3
                Bytenum = 2
        elif FrameState == 3:  # angle

            if Bytenum < 10:
                AngleData[Bytenum - 2] = data
                CheckSum += data
                Bytenum += 1
            else:
                if data == (CheckSum & 0xff):
                    Angle = get_angle(AngleData)
                    d = Angle
                CheckSum = 0
                Bytenum = 0
                FrameState = 0
        else:
            CheckSum = 0
            Bytenum = 0
            FrameState = 0
def turn():
    print("dis1:",dis1)
    print("dis2:",dis2)
    if dis1 <= 30 and dis2 >= 30:
        print("向右转")
        time.sleep(0.4)
        for i in range(90, 123, 5):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
        for i in range(122, 89, -5):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
    elif dis1 >= 30 and dis2 <= 30:
        print("向左转")
        time.sleep(0.4)
        for i in range(90, 57, -5):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
        for i in range(58, 91, 5):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
    elif dis1 <= 30 and dis2 <= 30:
        print("向左转")
        time.sleep(0.4)
        for i in range(90, 57, -10):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
        for i in range(58, 91, 10):
            pwm1.ChangeDutyCycle(40)
            pwm2.ChangeDutyCycle(i / 18 + 2.5)
            time.sleep(0.02)
            pwm2.ChangeDutyCycle(0)
            time.sleep(0.2)
    else:
        print("不需要转弯")
    return
def get_angle(datahex):
    ryl = datahex[2]
    ryh = datahex[3]
    k_angle = 180.0

    angle_y = (ryh << 8 | ryl) / 32768.0 * k_angle

    if angle_y >= k_angle:
        angle_y -= 2 * k_angle
    return angle_y


def loop():
    while (True):
        ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
        setup()
        datahex = ser.read(33)
        DueData(datahex)
        Angle = get_angle(AngleData)
        d = int(Angle)
        dis1 = distance(TRIG1, ECHO1)
        dis2 = distance(TRIG2, ECHO2)
        print("angle: ", d)
        if d >= 30:
            print("正在向下调整")
            for i in range(d+1, 0, -5):
                forward(0.01, 4)
                time.sleep(0.02)
            turn()
        elif d <= -30:
            print("正在向上调整")
            for i in range(d - 1, 0, 5):
                backward(0.01, 4)
                time.sleep(0.02)
            turn()
        else:
            print("不需要调整 angle: ",d)
            turn()

if __name__=='__main__':
    setup()
    try:
        dis1 = distance(TRIG1, ECHO1)
        dis2 = distance(TRIG2, ECHO2)
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        destroy()
