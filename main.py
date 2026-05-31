from validaciones import funciones
(
    mostrar_menu, validar_contra_vacia, validar_seguridad, contar_tipos_caracteres, buscar_caracter, contra_invertida, generar_reporte, verificar_palindromo) =  
    ,
    ,
    ,
    ,
    ,
    
)


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

