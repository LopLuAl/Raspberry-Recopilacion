import RPi.GPIO as GPIO     #EQUIVALENTE A EL INCLUDE EN ARDUINO
channel  = 19               # DECLARACION E INICIALIZACION DE UNA VARIABLE
channel2 = 26
GPIO.setmode(GPIO.BCM)      #USAMOS LA NUMERACION QUE TIENE EL PROCESADOR
                            #EN EL COBLER APARECERA COMO GPIOxx
GPIO.setup(channel,GPIO.OUT)#DECLARAMOS EL PIN x COMO SALIDA
GPIO.setup(channel2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #DECLARAMOS EL PIN x COMO ENTRADA
                                                         # Y HABILITAMOS LA  R DE PULL-UP
while True:
    if GPIO.input(channel2):
       print("Led prendido")
       GPIO.output(channel,True)
    else:
      GPIO.output(channel,False)
      print("Led apagado")
