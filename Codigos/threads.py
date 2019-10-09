import threading
def funcion():
    print("Hola mundo")
t = threading.Timer(1.0,funcion)#la funcion es llamada cada 1 seg
t.start()
