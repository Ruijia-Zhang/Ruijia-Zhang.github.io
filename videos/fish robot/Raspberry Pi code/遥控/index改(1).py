#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# encoding: utf-8
from bottle import get, post, run, request, route, template
import RPi.GPIO as GPIO
import time
import sys
####  定义Fish类
class Fish(object):
    def __init__(self):
        self.zhiliu_pin=[11,12,13,15,29]
        self.zhiliuin1_pin=self.zhiliu_pin[0]
        self.zhiliuin2_pin=self.zhiliu_pin[1]
        self.zhiliuin3_pin=self.zhiliu_pin[2]
        self.duojiin4_pin=self.zhiliu_pin[3]
        self.xiongqi_pin=self.zhiliu_pin[4]
        self.bujin_pin=[22,23,24,26]
    def front(self):
        print("开始运动")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        pwm1 = GPIO.PWM(self.zhiliuin2_pin, 80)
        pwm1.start(100)
        GPIO.output(self.zhiliuin1_pin, True)
        GPIO.output(self.zhiliuin3_pin, False)
        time.sleep(10)
        print("结束运动")
    def right(self):
        print("开始运动")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        pwm1 = GPIO.PWM(self.zhiliuin2_pin, 80)
        pwm1.start(70)
        GPIO.output(self.zhiliuin1_pin, True)
        GPIO.output(self.zhiliuin3_pin, False)
        GPIO.setup(self.duojiin4_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setup(self.duojiin4_pin, GPIO.OUT, initial=False)
        pwm2 = GPIO.PWM(self.duojiin4_pin, 50)
        pwm2.start(7.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(0.5)
        pwm2.ChangeDutyCycle(5.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(6)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(6.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(7)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(7.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(0.5)
    def left(self):
        print("开始运动")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        pwm1 = GPIO.PWM(self.zhiliuin2_pin, 80)
        pwm1.start(70)
        GPIO.output(self.zhiliuin1_pin, True)
        GPIO.output(self.zhiliuin3_pin, False)
        GPIO.setup(self.duojiin4_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setup(self.duojiin4_pin, GPIO.OUT, initial=False)
        pwm2 = GPIO.PWM(self.duojiin4_pin, 50)
        pwm2.start(7.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(9.4)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(9)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(8.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(8)
        pwm2.ChangeDutyCycle(0)
        time.sleep(1)
        pwm2.ChangeDutyCycle(7.5)
        pwm2.ChangeDutyCycle(0)
        time.sleep(0.5)
    def setStep(self,w1, w2, w3, w4):
        GPIO.output(self.bujin_pin[0], w1)
        GPIO.output(self.bujin_pin[1], w2)
        GPIO.output(self.bujin_pin[2], w3)
        GPIO.output(self.bujin_pin[3], w4)

    def forward(self,a):
        for i in range(0, a):
            Fish.setStep(self,1, 0, 1, 0)
            time.sleep(0.01)
            Fish.setStep(self,0, 1, 1, 0)
            time.sleep(0.01)
            Fish.setStep(self,0, 1, 0, 1)
            time.sleep(0.01)
            Fish.setStep(self,1, 0, 0, 1)
            time.sleep(0.01)
    def backward(self,b):
        for i in range(0, b):
            Fish.setStep(self,1, 0, 0, 1)
            time.sleep(0.01)
            Fish.setStep(self,0, 1, 0, 1)
            time.sleep(0.01)
            Fish.setStep(self,0, 1, 1, 0)
            time.sleep(0.01)
            Fish.setStep(self,1, 0, 1, 0)
            time.sleep(0.01)
    def down(self):
        print("开始运动")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        pwm1 = GPIO.PWM(self.zhiliuin2_pin, 80)
        pwm1.start(90)
        GPIO.output(self.zhiliuin1_pin, True)
        GPIO.output(self.zhiliuin3_pin, False)
        GPIO.setup(self.xiongqi_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setup(self.xiongqi_pin, GPIO.OUT, initial=False)
        pwm3 = GPIO.PWM(self.xiongqi_pin, 50)
        pwm3.start(0)
        time.sleep(2)
        pwm3.ChangeDutyCycle(9.4)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
        time.sleep(0.04)
        for pin in self.bujin_pin:
            GPIO.setup(pin,GPIO.OUT)
        for angle in range(0, -31, -10):
            Fish.backward(self,4)
            time.sleep(0.02)
            Fish.setStep(self,0,0,0,0)
        time.sleep(3)
        for angle in range(-30, 1, 10):
            Fish.forward(self,4)
            time.sleep(0.02)
            Fish.setStep(self,0,0,0,0)
        pwm3.ChangeDutyCycle(7.5)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
        time.sleep(0.04)
    def float(self):
        print("开始运动")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        pwm1 = GPIO.PWM(self.zhiliuin2_pin, 80)
        pwm1.start(90)
        GPIO.output(self.zhiliuin1_pin, True)
        GPIO.output(self.zhiliuin3_pin, False)
        GPIO.setup(self.xiongqi_pin, GPIO.OUT)
        GPIO.setwarnings(False)
        GPIO.setup(self.xiongqi_pin, GPIO.OUT, initial=False)
        pwm3 = GPIO.PWM(self.xiongqi_pin, 50)
        pwm3.start(0)
        time.sleep(2)
        pwm3.ChangeDutyCycle(5.5)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
        time.sleep(0.04)
        for pin in self.bujin_pin:
            GPIO.setup(pin, GPIO.OUT)
        for angle in range(0, 31, 10):
            Fish.forward(self,4)
            time.sleep(0.02)
            Fish.setStep(self,0,0,0,0)
        time.sleep(3)
        for angle in range(30, -1, -10):
            Fish.backward(self,4)
            time.sleep(0.02)
            Fish.setStep(self,0,0,0,0)
        pwm3.ChangeDutyCycle(7.5)
        time.sleep(0.04)
        pwm3.ChangeDutyCycle(0)
        time.sleep(0.04)
    def stop(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.zhiliuin1_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin2_pin, GPIO.OUT)
        GPIO.setup(self.zhiliuin3_pin, GPIO.OUT)
        GPIO.setup(self.duojiin4_pin, GPIO.OUT, initial=False)
        GPIO.setup(self.xiongqi_pin, GPIO.OUT, initial=False)
        for pin in self.bujin_pin:
            GPIO.setup(pin, GPIO.OUT)
        GPIO.cleanup()
####  定义main主函数
def main(status):
    fish = Fish()
    if status == "front":
        fish.front()
    elif status == "left":
        fish.left()
    elif status == "right":
        fish.right()
    elif status == "down":
        fish.down()
    elif status == "float":
        fish.float()
    elif status == "stop":
        fish.stop()

#### 收到浏览器请求，返回一个HTML文件。
@get('/')
def index():
    return template("/home/pi/fish/wificontrol/index.html") #### 此处输入html文件的具体目录。

#### 收到浏览器发来的指令。
@post("/cmd")
def cmd():
    adss = request.body.read().decode()
    print("put an order:" + adss)
    main(adss)
    return "OK"

#### 开启服务器，端口默认8080。
run(host="0.0.0.0",port="8081")
