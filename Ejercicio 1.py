import random

def validar_num(x):
    cuenta = 0
    for i in range(x):
        if x%(i+1) == 0:
            cuenta = cuenta + 1
    if cuenta%2 == 0:
        return False
    else:
        return True

print("Bienvenido al programa para validar si un numero es inteligente")

numeros = []
cantidad = int(input("Ingrese la cantidad de numeros que quiere validar: "))

for i in range(cantidad):
    aleatorio = random.randint(1,1000)
    numeros.append(aleatorio)

print("Los numeros a validar son : " + str(numeros))

for i in numeros:
    respuesta = validar_num(i)
    if respuesta == True:
        print( str(i) + " Si es inteligente")
    elif respuesta == False:
        print( str(i) + " No es inteligente")
      

