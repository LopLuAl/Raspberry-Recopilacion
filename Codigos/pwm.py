#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO     # importar el módulo como GPIO
channel  = 19               # DECLARACION E INICIALIZACION DE VARIBLES
channel2 = 26
channel3 = 17

frequency = 50
dc = 90

GPIO.setmode(GPIO.BCM)      #USAMOS LA NUMERACION QUE TIENE EL PROCESADOR
                            #EN EL COBLER APARECERA COMO GPIOxx
GPIO.setup(channel,GPIO.OUT)#DECLARAMOS EL PIN x COMO SALIDA
GPIO.setup(channel2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    #DECLARAMOS EL GPIO COMO ENTRADA
                                                            # Y HABILITAMOS LA  R DE PULL-DOWN
GPIO.setup(channel3,GPIO.OUT)


p = GPIO.PWM(channel3, frequency)   # instancia del objeto efecto con canal/Freq
p.start(dc)                         # DC es el ciclo de trabajo valores de 0 (0%) y 1 (100%)
p.ChangeDutyCycle(dc)               # cambio del ciclo de trabajo


while True:
    if GPIO.input(channel2):
      GPIO.output(channel,True)
      dc=20
    else:
      GPIO.output(channel,False)
      dc=50
    p.ChangeDutyCycle(dc)
