# MiPrograma.py
import random
 
# -----------------------------------------------------
Programa que suma todos los numeros pares que hay en la lista 
# -----------------------------------------------------
def sumarListaPares(lista):
    sum=0
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0:
            sum=sum+lista[i]
 
    return sum

# -----------------------------------------------------
# -----------------------------------------------------
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])

# -----------------------------------------------------
# -----------------------------------------------------
def crearLista():
    lista=[]
 
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 5)))
        i=i+1
    return lista

# -----------------------------------------------------
# -----------------------------------------------------
A = crearLista()
imprimirLista(A,"A")
print "Suma = " + str(sumarListaPares(A))

def sumarListaImpares(lista):sum=0
for i in range(0,len(lista)):
if lista[i] % 2 == 0:
sum=sum+lista[i]
return sum

#La parte sumarListaImpares funciona correctamente, suma los impares dentro del rango de la lista
