# CODE:40
import csv
import random
import interfaz


def leer_palabra_secreta(csvfilename):
    # Leer la palabra secreta de un archivo csv.
    with open(csvfilename, 'r') as csvfile:
        csvfile = csvfile.read().split('\n')
        data = list(csvfile)
    #print(data)
    
    data = random.choice (data)    
    return data 

def pedir_letra(letras_usadas):
    letra = input("Ingrese una letra: ")

    if len(letra) > 1:
        print("Letra invalida")
        letra = pedir_letra(letras_usadas)

    elif letra in letras_usadas:
        print(f"Usted ya ingreso la letra {letra}")
        letra = pedir_letra(letras_usadas)
    return letra

def verificar_letra(letra, palabra):
    if letra in palabra:
        return True
    else:
        return False    

def validar_palabra(letras_usadas, palabra_secreta):
    for i in palabra_secreta:
        if i not in letras_usadas:
            coincide = False
            break
        else:
            coincide = True
    return coincide        


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        letras_usadas.append(letra)    
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')  
