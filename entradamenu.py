import sys

minimo = 0
maximo = 0
intentoslim = 0
        
print("Estos son los modos de juego que hay: \n"
                "[1] Nivel simple: entre los números 0 y 100. \n"
                "[2] Nivel intermedio: entre los números 0 y 1.000. \n"
                "[3] Nivel avanzado: entre los números 0 y 1.000.000. \n"
                "[4] Nivel experto: entre los números 0 y 1.000.000.000.000. \n")

while True:
        nivel = input("Elija un de ellos para jugar escribiendo 1, 2,3 o 4: ")      #Aquí hago al jugador elegir el nivel que quiere juegar.

        if nivel.isdigit():         #Compruebo que se haya introducido un número entre 1 y 4 (los niveles que hay).
            try:
                nivel = int(nivel)
                    
                if nivel <= 1:          #Dependiendo del nivel elegido, el rango es diferente y el numero de intentos varía.
                    maximo = maximo + 100
                    intentoslim = 20
                    break
                elif nivel <= 2:
                    maximo = maximo + 1000
                    intentoslim = 15
                    break
                elif nivel <= 3:
                    maximo = maximo + 1000000
                    intentoslim = 10
                    break
                elif nivel <= 4:
                    maximo = maximo + 1000000000000
                    intentoslim = 5
                    break

            except ValueError:
                print ("La entrada es incorrecta.")

            while not 0 < nivel < 5:
                print("No ha introducido un numero entre el 1 y el 4. \n")
                break

        else:
            print("Introduce un nivel válido (entre 1 y 4). \n")

       
    

