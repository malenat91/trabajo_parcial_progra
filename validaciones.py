def mostrar_menu() -> None:
    """
    Muestra el menú del programa al usuario,
    para que visualice las opciones disponibles
    """

    print("***********************************")
    print("1- Validar nivel de seguridad")
    print("2- Contar tipos de caracteres")
    print("3- Buscar carácter específico")
    print("4- Mostrar contraseña invertida")
    print("5- Generar reporte estadístico")
    print("6- Verificar si es palíndromo")
    #print("7- Ordenar caracteres de la contraseña")
    print("7- Salir")
    print("***********************************")
def validar_contra_vacia(contraseña: str) -> str:
    """
    valida que la contraseña cumpla con todo lo solicitado:
    -que tenga al menos 8 caracteres
    -que no comience con espacios
    -que contenga al menos una letra

    devuelve (return) una contraseña válida.
    """
    es_valida = False #while flag

    while es_valida == False:
        tiene_letra = False
   
        for i in range(len(contraseña)):

            letra = contraseña[i]

            if (letra >= "A" and letra <= "Z" or letra >= "a" and letra <= "z"):
                    tiene_letra = True

        if len(contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres")

        elif contraseña[0] == " ":
            print("La contraseña no puede comenzar con espacio")
            
        elif tiene_letra == False:
            print("La contraseña debe contener al menos una letra")

        else:
            print("Contraseña válida")
            return contraseña

        contraseña = input("Ingrese otra contraseña: ")       
def validar_seguridad(contraseña: str) -> None:
    """
    verifica si la contraseña es débil, media o fuerte.
    """
    solo_letras = True
    letras_y_numeros = False
    tiene_simbolos = False

    for i in range(len(contraseña)):

        letra = contraseña[i]

        if letra >= "A" and letra <= "Z" or letra >= "a" and letra <= "z":
            pass

        elif letra >= "0" and letra <= "9":
            solo_letras = False
            letras_y_numeros = True

        else:
            solo_letras = False
            tiene_simbolos = True
            letras_y_numeros = True


    if len(contraseña) >= 12 and tiene_simbolos == True and letras_y_numeros == True:
        print("********************\nLa contraseña es fuerte\n********************")

    elif letras_y_numeros == True or tiene_simbolos == True:            
        print("********************\nLa contraseña es media\n********************")

    elif len(contraseña) >= 8 and len(contraseña) <= 9 and solo_letras == True:
        print("********************\nLa contraseña es débil\n********************")
def contar_tipos_caracteres(contraseña: str) -> None:
    """
    cuenta la cantidad de letras, números,
    símbolos y espacios de la contraseña
    """
    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0
    cantidad_espacios = 0

    for i in range(len(contraseña)):

        letra = contraseña[i]

        if letra >= "A" and letra <= "Z" or letra >= "a" and letra <= "z":

            cantidad_letras += 1

        elif letra >= "0" and letra <= "9":

            cantidad_numeros += 1

        elif letra == " ":

            cantidad_espacios += 1

        else:

            cantidad_simbolos += 1


    print(f"********************\nCantidad de letras: {cantidad_letras}\n********************")
    print(f"********************\nCantidad de números: {cantidad_numeros}\n********************")
    print(f"********************\nCantidad de símbolos: {cantidad_simbolos}\n********************")
    print(f"********************\nCantidad de espacios: {cantidad_espacios}\n********************")
def buscar_caracter(contraseña: str) -> None:
    """
    busca un carácter específico solicitado al usuario
    dentro de la contraseña
    y muestra sus posiciones y cantidad de apariciones
    """
    caracter_buscado = input("Ingrese un carácter: ")
    contador_caracter = 0

    print("Posiciones encontradas:")

    for i in range(len(contraseña)):

        if contraseña[i] == caracter_buscado:

            contador_caracter += 1
            print(i)

    print(f"Cantidad de veces que aparece: {contador_caracter}")
def contra_invertida(contraseña: str) -> None:
    """
    invierte la contraseña manualmente,
    muestra la contraseña invertida.
    """
    invertida = "" #guarda la variable para la contraseña invertida (crea una cadena vacía)

    for i in range(len(contraseña) - 1, -1, -1): #(inicio, fin, salto), va de atras hacia adelante de a 1, frenando en el primer caracter
        invertida += contraseña[i]
    print(f"Contraseña original: {contraseña}, contraseña invertida: {invertida}")
def generar_reporte(contraseña: str) -> None:
    """
    genera un reporte estadístico de la contraseña:
    longitud, porcentajes y repeticiones consecutivas
    """
    print("Resporte estadistico: ")
    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0
    cantidad_repeticiones = 0

    longitud_total = len(contraseña)

    for i in range(len(contraseña)): #verifica cada caracter de la contraseña


        caracter = contraseña[i]
        #CANTIDAD DE CADA UNO
        if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z"):
            cantidad_letras += 1

        elif caracter >= "0" and caracter <= "9":
            cantidad_numeros += 1

        else:
            cantidad_simbolos += 1

    print(f"Longitud total: {longitud_total}")


    #PORCENTAJES    
    porcentaje_letras = cantidad_letras * 100 / longitud_total #no hace falta aclarar el tipo de dato porque la division ya lo genera
    porcentaje_numeros = cantidad_numeros * 100 / longitud_total
    porcentaje_simbolos = cantidad_simbolos * 100 / longitud_total

    print(f"Porcentaje de letras: {porcentaje_letras}%")
    print(f"Porcentaje de números: {porcentaje_numeros}%")
    print(f"Porcentaje de símbolos: {porcentaje_simbolos}%")

    print("Repeticiones consecutivas:")

    for i in range(len(contraseña) - 1): #verifica cada caracter de la contraseña

        if contraseña[i] == contraseña[i + 1]:

            cantidad_repeticiones += 1

            print(f"1 repetición de {contraseña[i]}") #ver como poner la cantidad total de cada caracter

    print(f"Cantidad total de repeticiones: {cantidad_repeticiones}")
def verificar_palindromo(contraseña: str) -> None:
    """
    verifica si la contraseña es un palíndromo
    """
    #reutilizo codigo de contra_invertida
    invertida = "" #guarda la variable para la contraseña invertida (crea una cadena vacía)

    for i in range(len(contraseña)- 1, -1, -1): #(inicio, fin, salto), va de atras hacia adelante de a 1, frenando en el primer caracter
        invertida += contraseña[i]
    print(f"Contraseña original: {contraseña}\nContraseña invertida: {invertida}")
    if contraseña == invertida:
        print("Las contraseñas se leen igual de derecha a izquierda: es palíndromo")
    else:
        print("Las contraseñas no se leen igual de derecha a izquierda: no es palíndromo")