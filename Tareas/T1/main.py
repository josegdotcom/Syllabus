import dccultivo as dcc
import utils

if __name__ == "__main__":
    mis = dcc.DCCultivo()
    data_predios = []
    menu = "p_menu"
    list_predios = []
    mis.crear_predios("prepredios.txt")

    while True:
        ya = (len(mis.predios) > 0)

        if menu == "p_menu" and not ya:
            print("Welcome to Dccultivos")
            print("El mejor lugar conseguir unos tacos :)")
            print("\nQue quieres hacer primero?")
            print('("tacos") Lest Play   ("chao") Porque te irias?')

            user_input = input()
            if user_input == "tacos":
                if not ya:
                    menu = "crear_predio"
                else:
                    menu = "p_menu"
            elif user_input == "chao":
                print("en ese caso no quieres tacos, bye bye *escoria*")
                print("Mentira. Te quiero ;o")
                break
            else:
                print(f"No veo a {user_input} en tus funciones")

        elif menu == "p_menu" and ya:
            print("A trabajar!")
            print("tu terrenos esta listo para trabajar")
            print("\nque vas a hacer?")
            print("""
                [1] visualizar predios
                [2] plantar
                [3] regar
                [4] buscar y eliminar plagas
                [5] bueno adios""")

            opcion = input()
            if opcion == "1":
                menu = "ver predios"
            elif opcion == "2":
                menu = "plantar"
            elif opcion == "3":
                menu = "regar"
            elif opcion == "4":
                menu = "buscar_eliminar_plagas"
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print(f"no veo a {opcion} en tus acciones")
                
        elif menu == "ver predios":
            if not data_predios:
                print("No hay nada por aqui")
                menu = "p_menu"
            else:
                print(f"¿Cuál de estos quieres ver?\n{data_predios}")
                predio_name = input()
                menu = "p_menu"

        elif menu == "plantar":
            parametor = 1
            while parametor == 1:
                print("Primero, indica el ancho del área a plantar:")
                print('Si quieres devolverte: escribe "back"')
                ancho = input()

                if ancho.isdigit() and int(ancho) > 0:
                    print("\nExcelente, sigamos.")
                    parametor += 1
                elif ancho == "back":
                    menu = "p_menu"
                    break
                else:
                    print("Por favor, ingresa un número válido para el ancho.")

            while parametor == 2:
                print("Ahora, indica el largo del área a plantar :o")
                print('Si quieres cambiar el ancho: escribe "back"')
                largo = input()

                if largo.isdigit() and int(largo) > 0:
                    print("Muy bien, sigamos...")
                    parametor += 1
                elif largo == "back":
                    parametor -= 1
                else:
                    print("Por favor, ingresa un número válido para el largo.")

            while parametor == 3:
                print("Indica qué planta quieres plantar (del 1 al 9):")
                print('Si quieres devolverte: escribe "back"')
                name = input()

                if name.isdigit() and 1 <= int(name) <= 9:
                    print(f"\nExcelente, planta {name} seleccionada, nada ilegal aqui ('_')")
                    resultado = mis.buscar_y_plantar(name, int(largo), int(ancho))
                    name = None; ancho = None; largo = None
                    
                    if resultado == True:
                        print("¡Vamos, hemos logrado plantar!")
                    else:
                        print("No se pudo plantar la policia requiso tu plantacion")
                    parametor = 0
                    menu = "p_menu"
                elif name == "back":
                    parametor -= 1
                else:
                    print("Por favor, ingresa un numero entre 1 y 9.")
                    
        elif menu == "regar":
            print("Ingresa el código del predio:")
            codigo_predio = input()
            print("Ingresa las coordenadas de riego y para acomodarte la vida y que ya estoy cansado :( (separadas por espacio, por ejemplo: 2 3):")
            coordenadas = list(map(int, input().split(" ")))
            print("Ingresa el área de riego: (como un numero)")
            area = int(input())
            
            mis.buscar_y_regar(codigo_predio, coordenadas, area)
            print("¡Todo bien mojado su senor/ra/re/.../ru!")
            
            menu = "p_menu"
            
        elif menu == "buscar_eliminar_plagas":
            print("QUE SE ARMEN LOS PUTASOS!!!")
            print("primero las coordenadas y por ultimo código de plaga que quieres meterle un headshot (por ejemplo: 2 3 1):")
            plaga_info = list(map(int, input().split()))
            lista_plagas = []
            
            # Suponiendo que el formato es coordenadas (i, j) y código de plaga
            for i in range(0, len(plaga_info), 3):
                coordenada_i = plaga_info[i]
                coordenada_j = plaga_info[i + 1]
                codigo_plaga = plaga_info[i + 2]
                lista_plagas.append([codigo_plaga, [coordenada_i, coordenada_j]])
            
            resultados = mis.detectar_plagas(lista_plagas)
            print("Resultados del exterminio de plagas:")
            for resultado in resultados:
                print(f"Predio: {resultado[0]}, Celdas eliminadas: {resultado[1]}")
            
            print("¡exterminio de plagas realizada exitosamente!")
            menu = "p_menu"

        elif menu == "crear_predio":
            parametor = 1
            
            while parametor == 1:
                print("\nPrimero, ¿qué nombre le pondrás al predio?")
                print('Si quieres devolverte: escribe "back"')
                print('Por ende el nombre de tu predio no puede ser "back"')
                name = input()

                if name == "back":
                    menu = "p_menu"  # Regresa al menú principal
                    break
                
                if name not in [predio.codigo_predio for predio in mis.predios]:
                    print(f"\nNombre {name} asignado al predio. Sigamos...")
                    parametor += 1
                else:
                    print("Ese nombre ya lo utilizaste. Se más original")

            while parametor == 2:
                print("¿Qué ancho tendrá el predio?")
                print('Si quieres cambiar el nombre: escribe "back"')
                ancho = input()

                if ancho.isdigit() and int(ancho) > 0:
                    print("\nAncho válido. Sigamos...")
                    parametor += 1
                elif ancho == "back":
                    parametor -= 1
                else:
                    print("Por favor, ingresa un número válido para el ancho")

            while parametor == 3:
                print("¿Qué largo tendrá el predio? :o")
                print('Si quieres cambiar el ancho: escribe "back"')
                largo = input()

                if largo.isdigit() and int(largo) > 0:
                    print("¡Muy bien, a trabajar!")
                    new_predio = dcc.Predio(name, int(largo), int(ancho))
                    new_predio.crear_plano("normal")  # Especifica el tipo de plano
                    new_predio.crear_plano("riego")  # Especifica el tipo de plano
                    data_predios.append(name)
                    list_predios.append(new_predio)
                    mis.predios = list_predios
                    name = None; ancho = None; largo = None
                    parametor = 0
                    menu = "p_menu"  # Cambia a menú principal después de agregar el predio
                elif largo == "back":
                    parametor -= 1
                else:
                    print("Por favor, ingresa un número válido para el largo.")