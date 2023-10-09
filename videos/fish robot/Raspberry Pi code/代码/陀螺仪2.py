#encoding: utf-8
#运行前需先安装pyserial，用WIN+R调出运行框，输入CMD，进入命令行，输入pip install pyserial更新一下函数库

import serial

AngleData=[0.0]*8          
FrameState = 0            #通过0x后面的值判断属于哪一种情况
Bytenum = 0               #读取到这一段的第几位
CheckSum = 0              #求和校验位         

Angle = [0.0]*3
def DueData(inputdata):   #新增的核心程序，对读取的数据进行划分，各自读到对应的数组里
    global  FrameState    #在局部修改全局变量，要进行global的定义
    global  Bytenum
    global  CheckSum
    global  Angle
    for data in inputdata:  #在输入的数据进行遍历
        #Python2软件版本这里需要插入 data = ord(data)*****************************************************************************************************
        if FrameState==0:   #当未确定状态的时候，进入以下判断
            if data==0x55 and Bytenum==0: #0x55位于第一位时候，开始读取数据，增大bytenum
                CheckSum=data
                Bytenum=1
                continue
            elif data==0x51 and Bytenum==1:#在byte不为0 且 识别到 0x51 的时候，改变frame
                CheckSum+=data
                FrameState=1
                Bytenum=2
            elif data==0x52 and Bytenum==1: #同理
                CheckSum+=data
                FrameState=2
                Bytenum=2
            elif data==0x53 and Bytenum==1:
                CheckSum+=data
                FrameState=3
                Bytenum=2
        elif FrameState==3: # angle
            
            if Bytenum<10:
                AngleData[Bytenum-2]=data
                CheckSum+=data
                Bytenum+=1
            else:
                if data == (CheckSum&0xff):
                    Angle = get_angle(AngleData)
                    d = Angle
                    print("Angle(deg):%10.3f"%d)
                CheckSum=0
                Bytenum=0
                FrameState=0
        else:
            CheckSum = 0
            Bytenum = 0
            FrameState = 0
def get_angle(datahex):
    ryl = datahex[2]                                        
    ryh = datahex[3]
    k_angle = 180.0

    angle_y = (ryh << 8 | ryl) / 32768.0 * k_angle

    if angle_y >= k_angle:
        angle_y -= 2 * k_angle
    return angle_y
 
 
if __name__=='__main__':
     # use raw_input function for python 2.x or input function for python3.x
    
    ser = serial.Serial("/dev/ttyUSB0",115200, timeout=0.5)  # ser = serial.Serial('com7',115200, timeout=0.5) 
    print(ser.is_open)
    while(1):    
        datahex = ser.read(33)
        DueData(datahex)
        