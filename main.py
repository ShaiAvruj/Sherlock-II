#Ejercicio 1
def digitos(numero_de_tarjeta: str) -> int:
    return len(numero_de_tarjeta)

#Ejercicio 2
def obtener_prefijo(numero_de_tarjeta: str, tamaño_prefijo: int) -> int:
    prefijo = int(numero_de_tarjeta[:tamaño_prefijo])
    return prefijo

#Ejercicio 3
def tipo_tarjeta(numero_de_tarjeta: str) -> str:
    num_digitos = digitos(numero_de_tarjeta)
    prefijo = obtener_prefijo(numero_de_tarjeta, 2) # Se obtienen los primeros 2 dígitos

    if num_digitos == 15 and (prefijo == 34 or prefijo == 37):
        return "American Express"
    elif num_digitos == 16 and (prefijo <= 55 and prefijo >= 51): 
        return "Mastercard"
    elif num_digitos in [13, 16] and str(prefijo)[0] == '4':
        return "Visa"
    else:
        return'Invalid'

#Ejercicio 4
def digitos_impares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-1, -1, -2)]
    return digitos

#Ejercicio 5
def digitos_pares(numero_de_tarjeta: str) -> list[int]:
    digitos = [int(numero_de_tarjeta[i]) for i in range(len(numero_de_tarjeta)-2, -1, -2)]
    return digitos

#Ejercicio 6
def sumar_digitos(lista_digitos: list[int]) -> int:
    suma = 0

    for numero in lista_digitos:
        numero_str = str(numero) # Convertir el número a string
        for digito in numero_str:
            suma += int(digito) # Sumar cada dígito a la suma total

    return suma

#Ejercicio 7
def luhn(numero_de_tarjeta : str) -> bool:
    lista_digitos_pares= digitos_pares(numero_de_tarjeta)
    suma = 0

    for x in range(len(lista_digitos_pares)):
        lista_digitos_pares[x]*=2

    suma += sumar_digitos(lista_digitos_pares)
    lista_digitos_impares = digitos_impares(numero_de_tarjeta)
    suma += sumar_digitos(lista_digitos_impares)

    if suma % 10 == 0 : 
        return True
    else:
        return False


#Ejercicio 8
def validar_tarjeta(numero_de_tarjeta : str) -> bool:
    Luhn = luhn(numero_de_tarjeta)
    Is_Valid_Card = tipo_tarjeta(numero_de_tarjeta)
    if  Luhn == True:
        if Is_Valid_Card != "Invalid" :
            return True
        else:
            return False
    else:
        return False