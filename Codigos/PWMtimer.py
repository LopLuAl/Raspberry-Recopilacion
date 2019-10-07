#!/usr/bin/env python
# -*- coding: utf-8 -*-
canal = 25
canal_pwm = 13
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(canal,GPIO.OUT)
GPIO.setup(canal,GPIO.IN)
GPIO.setup(canal,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(canal_pwm,GPIO.OUT)
p = GPIO.PWM(canal_pwm,300)
x=0
p.start(x)

while True:
    p.ChangeDutyCycle(x)
    time.sleep(0.1)
    x = x + 5
    print(x)
    if x >100:
        print("Es el MAX",x)
        x = 0
        time.sleep(0.5)
    
    
 

###p.stop()
###
    
