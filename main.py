from validaciones import contar_tipos_caracteres, generar_reporte, buscar_caracter, contra_invertida, validar_contra_vacia, validar_seguridad, verificar_palindromo, mostrar_menu


contraseña = input("¡Bienvenidx! Por favor, ingrese su contraseña: ")
contraseña = validar_contra_vacia(contraseña)
opcion = 0


while opcion != 7:
    mostrar_menu()

    opcion = int(input("Seleccione la opcion que desea ejecutar: "))

    match opcion:     
        case 1: validar_seguridad(contraseña)

        case 2: contar_tipos_caracteres(contraseña)

        case 3: buscar_caracter(contraseña)

        case 4: contra_invertida(contraseña)

        case 5: generar_reporte(contraseña)

        case 6: verificar_palindromo(contraseña)

        # case 7: ordenar_caracteres(contraseña)

        case 7: print("Saliendo del sistema")

        case _: print("Opción inválida")

