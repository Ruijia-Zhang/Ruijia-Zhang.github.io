import RPi.GPIO as GPIO
import time

pin_avoid_obstacle = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_avoid_obstacle,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        status = GPIO.input(pin_avoid_obstacle)
        if status == TRUE:
            print(' ')
        else:
            print('')
        time.sleep(0.5)
except KeyboradInterrupt:
    GPIO.cleanup()
