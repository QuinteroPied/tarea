# Esta función recibe un número entero n y devuelva la suma de todos los números primos menores o iguales a n.

# Definimos la función de un numero primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Definimos la sumatoria de los numeros primos menores o iguales a n
def suma_primos(n):
    suma=0
    for i in range(0,n):
        if es_primo(i)==True:
            suma+=i
    return suma

print(suma_primos(30))
