import sys

from entradamenu import *    #Importo el menú.

def elegir_numero_a_adivinar():
    SI = ("s", "si", "y", "yes", "1")       #Defino algunas variables que me seran útiles para el juego.
    intentos = 0
    puntos = 100
    ayuda = minimo 
    ayuda2 = maximo
    
    while True:         #En este while dejo que se elija el número que quieren que se adivine.
        print("")
        numerosecreto = input(f"Introduzca el número a adivinar entre {minimo} y {maximo}: ")

        if numerosecreto.isdigit():         #Compruebo que sea un número y que este entre el mínimo y el máximo de ese nivel.
            try:
                numerosecreto = int(numerosecreto)
                break

            except ValueError:
                print ("La entrada es incorrecta.")

            while not minimo < numerosecreto < maximo:
                print(f"No ha introducido un numero entre {minimo} y {maximo}. \n")
                break
            
        else:           #Si no es un número tiene que volver a poner el numero que quiere que se adivine.
            print("Introduce un nivel válido (entre 1 y 4). \n")

    print("")
    print(f"Tienes {intentoslim} intentos.")


    while True:         #En este while se da el juego: poner números hasta adivinarlo.
        numero = input(f"Introduzca un número entre el {minimo} y el {maximo}. Si quieres una ayudita, escriba 'ayuda': ")
        print ("")

        if intentos == intentoslim:         #Aquí defino que si llegas al número máximo de intentos de ese nivel pierdes.
            print(f"No has adivinado el número en {intentoslim} intentos. Has perdido.")
            input("¿Quieres volver a jugar?") 
            volverajugar = input("¿Desea jugar una nueva partida? ")
            
            while True:         #En este while hago que te permita elegir si volver a jugar o no.
                if volverajugar == SI(0, 1, 2, 3, 4, 5):
                    return elegir_numero_a_adivinar()
                else: 
                    print("¡Hasta pronto!") 
                    sys.exit()
                        

        if numero == "ayuda":   #Aquí permito al jugador perdir unaayuda que te marca cual es el mínimo y el máximo.
            print(f"Tu numero esta entre {ayuda} y {ayuda2}. \n")
            pass

        else:                   #Si no se pide la ayuda compara el numero para saber si ha ganado o no.
            if numero.isdigit():        #Aquí se comprueba si has introducido un número entre el mínimo y el másimo de ese nivel.
                try:
                    numero = int(numero) 

                except ValueError:
                    print ("La entrada es incorrecta.")

                while not minimo <= numero <= maximo:
                    print(f"No ha introducido un numero entre {minimo} y {maximo}. \n")
                    break

                intentos = intentos + 1
                
                #Una vez se comprueba que has introducido un númer correcto, se decide si has ganado o no:
                if numerosecreto == numero:         #Aquí se comprueba si has ganado.  
                    print("¡Enhorabuena! Has adivinado el número. ")
                    print(f"Tus intentos para adivinarlo han sido {intentos}. \n")      #Si sí, te felicita y te da tu número de intentos.

                    nombre = input("¿Cuál es tu nombre? ")              #Te pido el nombre para hacer la tabla.
                    if intentos == 1:                                   #Hace la tabla según la puntuacion.
                        puntos = (f"TABLA DE PUNTUACIONES: \n"
                                    "{nombre} || {puntos} puntos.")
                        print(puntos)
                    else:
                        puntos = (f"TABLA DE PUNTUACIONES: \n"
                                    f"{nombre} || {100-intentos*5} puntos.")
                        print(puntos)

  
                    volverajugar = input("¿Quieres volver a jugar? ")   #Una vez presentada la tabla y los puntos te propone volver a jugar.
                    if volverajugar == SI(0, 1, 2, 3, 4, 5):
                        return elegir_numero_a_adivinar()

                    else: 
                        print("¡Hasta pronto!")                         #Si decides no volver a jugar se cierra el programa.
                        sys.exit() 

                else:
                    if numero > numerosecreto:
                        print(f"Tu numero es mayor que el numero a adivinar. ")
                        ayuda2 = numero
                    
                    else:
                        print(f"Tu numero es menor que el numero a adivinar. ")
                        ayuda = numero

            else:
                print("No has conseguido ni introducir un número... prueba otra vez. \n")

elegir_numero_a_adivinar()
