#En este ejercicio practicarás las estructuras de control, para ello deberás crear: 
# Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
# Pista: Los números inferiores a 0 son negativos y los superiores, positivos 
# Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que 
# tendrá el bucle deberá:
# Incrementar el valor de la variable en uno cada vez que se ejecute.
#Mostrarlo por pantalla cada vez que se ejecute.
#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez. 
#  Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o
#  menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla. 
# Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. 
# Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está.
#  También habrá que poner un default para cuando el valor de la variable no sea una estación.
#caso de problema if
print("Hola herramineta para revisar numero mayores o menores ")
num = input("Hola ingresa un numero: ")
num = float(num)
if num >= 0:
    print("El numero es mayor ")
else: 
    print("El numero es menor ")

#Caso de while
print("Caso de problema while ") 
numero = 3
while num <= 5:
    print(numero)
    numero = numero + 1
print("Terminado")
#Caso do while no hay en py
#caso de problema for

print("""Para el bucle For, crea una variable numeroFor, 
esta variable tendrá como valor 0 y su condición será que la variable sea igual o  menor que 3, 
se irá incrementando en 1 su valor cada vez que se ejecute y 
deberá mostrarse por pantalla. Hola herramineta para revisar numero mayores o menores """)
print("Hola incementaremos un numero")
numero = 0
for numero in range(3):
    numero += 1
    print(numero)
print("Programa Terminado")
