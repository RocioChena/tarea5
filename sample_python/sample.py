def ingresar_calificacion():
    while True:
        print("Por favor ingresa tu calificación de 1 a 5")
        entrada = input()
        if entrada.isnumeric():
                    calificacion = int (entrada)
                    if calificacion <= 0 or calificacion > 5:
                        print ("Por favor ingrese del 1 al 5")
                        
                    else:
                        print("Por favor ingresa tu comentario")
                        comentario = input()
                        post = f'Calificacion: {calificacion} Comentario: {comentario}'
                        with open("data.txt", 'a') as file_pc:
                            file_pc = open("data.txt", 'a')
                            file_pc.write(f'{ post } \n')
                            file_pc.close()
                        break   
        else:
                    print("Ingrese los puntos de calificación en números")

def comprobar_resultado():
    try:
                with open("data.txt", "r") as read_file:
                    print("Resultados hasta ahora")
                    read_file = open("data.txt", "r")
                    print( read_file.read() )
                    read_file.close()
    except FileNotFoundError:
                print("No hay resultados hasta ahora")

def mostrar_menu():
    while True:
        print("Por favor seleccione la acción que desea realizar")
        print("1: Ingresar puntos de evaluación y comentarios")
        print("2: Comprueba los resultados hasta el momento")
        print("3:Fin")
        numero= input()
        if numero.isnumeric():
            numero = int(numero)
            if numero == 1:
                ingresar_calificacion()
            elif numero == 2:
                comprobar_resultado()
            elif numero == 3:
                print("Terminar")
                break
            else:
                print("ingrese un valor del 1 al 3")
        else:
            print("ingrese 1 a 3")
            
mostrar_menu()
