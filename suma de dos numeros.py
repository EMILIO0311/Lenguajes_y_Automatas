'''
#string
nombre="Emilio"
print(0,1)

#SUMA DE DOS NUEMROS:
# Pedir al usuario que ingrese dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Realizar la suma de los dos números
suma = numero1 + numero2

# Mostrar el resultado
print("La suma de", numero1, "y", numero2, "es:", suma)

#USO DE CONDICIONES (IF)
x=int(input("Ingresa el primer número: "))
y="A"
z="B"
if x == 7:
    print(y)
elif x == 10:
    print(z)
else:
    print("este numero no existe")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

print("Minicalculadora")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")

print("3. Multiplicación")
print("4. División")

opcion = int(input("Seleccione una operación (1/2/3/4): "))

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    resultado = suma(num1, num2)
    signo = "+"
elif opcion == 2:
    resultado = resta(num1, num2)
    signo = "-"
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
    signo = "*"
elif opcion == 4:
    resultado = division(num1, num2)
    signo = "/"
else:
    resultado = "Opción inválida"
    signo = ""

if resultado != "Opción inválida":
    print(f"{num1} {signo} {num2} = {resultado}")
else:
    print(resultado)

nombre="Emilio"
for letra in nombre:
    print(letra)

texto="hola que onda como estas"
print("estas" in texto)
if "chorrito"
    '''



""""
'son las 7 de la noche y ya me quiero ir'
si encuentra el numero 7 y es menor a 8 imprime el numero 7 convertido a int y el texto, 'es hora de irnos son las: 7' 
"""
"""
texto = "son las 7 de la noche y ya me quiero ir"
numero = "7"
if numero in texto and int(numero) < 8:
    print(f"Es hora de irnos, son las: {numero}")
else:
    print("No se cumple la condición")
    """
"""
# Slicing string.
b = "Hola Mundo"
# Slice por rango.
print(b[5:10])
# Slice desde el inicio.
print(b[5:])
# Slice con posiciones negativas
print(b[-5:-2])

#Boleanos
# Mayor que
print(10>9)
#Igual que
print(10==9)
# Menor que
print(10<9)
# Variables boleanas
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("Vender Productos")
else:
    print("No vender")

tieneEfectivo=False
tieneTarjeta=False

if tieneEfectivo and tieneTarjeta:
    print("Decidace en tarjeta o efectivo XD")
elif tieneEfectivo:
    print("Pago en efectivo aceptado")
elif tieneTarjeta:
    print("Pago por tarjeta aceptado")
else:
    print("Error en venta")
#
isUploaded=True
if not isUploaded:
    print("REINTENTAR")
"""

#Operadores aritmeticos.

x=5
y=6
#suma
print(x+y)
#resta
print(x-y)
#multiplicacion
print(x*y)
#division
print(x/y)
#modulo
print(x%y)
#exponentes
print(x**y)
#floor division
print(x//y)
#operadores de asignacion
e=30
e+=32
e-=2
e*=2
e/=2
print(e)
#operadores logicos de comparacion
r=3
t=2
#igual
print(r==t)
#diferente
print(r!=t)
#mayor
print(r>t)
#menor
print(r<t)
#mayor igual
print(r>=t)
#menor igual
print(r<=t)

#operadores logicos
promedio=100
asistencias=True
aprobado=(promedio>70) and asistencias
#and, or, not
print(aprobado)

#operadores de identidad
j="hola"
k="hola "
print(j is k)
print(j is not k)
#funcion de reemplazo
print(k.replace(" ",""))
#operadores de pertenencia
print("A" in "HOLA")
print("A" not in "HOLA")

#lista
frutas=["manzana","Banana", "Mango"]
frutas2= ["😊","🤩","😀"]
print(frutas)
print(frutas2)
lista=[1,2,3,4,5,6]
logico=[True,False,True]
lista1=["abc",34,True,'a',"❤️"]
print(type(lista))
print(lista1)

#list, Tuple, Set, Dictionary
"""
#list: es una colecion la cual esta ordenada
y modificable, la cual permite duplicados

Tuple: Es una coleccion la cual esta ordenada y
no es modificable. Permite duplicados

Set: Es una coleccion la cual NO❌ esta ordenada y 
no es modificable ni indexada. NO ❌ permite duplicados

Dictionary: Es una coleccion la cual esta ordenada
es modificable.No permite duplicados
"""
"""

"""
"""
#Lista
lista1=["🦁","🐒","🐷","🐷"]
lista1.insert(3,"🐔")
lista1[2]="🐇"
print(lista1)
#Tuple (no da la opcion de insertar)
tupla1=("🦁","🐒","🐷")
print(tupla1)
#Set
set1={"🦁","🐒","🐷"}
set1.add("🦍")
set1.add("🐎")
set1.add("🐅")
print(set1)

#Diccionario
diccionario1={
    "leon":"🦁",     ## clave valor , o llave-- valor
    "monito":"🐒",
    "cerdito":"🐷"
}
diccionario1["koala"]="🐨"
diccionario1["tigre"]="🐯"
print(diccionario1["monito"])
print(diccionario1)
"""

"""
#0.CREAR UNA LISTA: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2.CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
NUMEROS UNICOS, SUMA TOTAL LISTA,VALOR SUMA TOTAL SET
MAXIMO , MINIMO VALOR
#4.IMPRIMIR LAS ESTADISTICAS
"""

#0.CREAR UNA LISTA: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
numeros=[1,2,5,3,2,3,3,6,10,8,9]
print(numeros)
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
convertirSet=set(numeros)
print(convertirSet)
#2.CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
sumaLista=sum(numeros)
print(sumaLista)
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
sumaSet= sum(convertirSet)
print(sumaSet)
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
#NUMEROS UNICOS, SUMA TOTAL LISTA,VALOR SUMA TOTAL SET
#MAXIMO , MINIMO VALOR
estadisticas = {
    "Numeros Unicos": len(convertirSet),
    "Suma Total Lista": sumaLista,
    "Suma Total Set": sumaSet,
    "Maximo Valor": max(numeros),
    "Minimo Valor": min(numeros)
}
# 4.Imprimir las estadísticas
for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")

# CONDICIONES

a=200
b=33

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

# Ciclo while - mientras
quiereVolver = True
vecesRegresaron= 1
while vecesRegresaron <= 3:
    print("Han vuelto " + str(vecesRegresaron)+ " veces")
    vecesRegresaron +=1


i=1
while i< 6:
    print(i)
    if i==3:
        break
    i+=1
print("continue")


# continue
i=0
while i< 6:
    i+=1
    if i == 3:
        continue
    print(i)

## foto

## ciclo for- for each
frutas= ["🍉","🍊","🍒"]

# for- Por cada
buscar = True
if buscar:
    for fruta in frutas:
        if fruta == "🍉":
            print("Se encontró: " + fruta)

        else:
            print("No Coincide")
else:
    print("NO SE ESTA BUSCANDO")



