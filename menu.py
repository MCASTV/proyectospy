print("Bienvenido @usuario")
print("Vamos a scrapear el siguiente pagina")
print("https://tiendapanini.com.mx/figuras")
print("----------")
print("Menu")

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Guardar en csv', accion1),
        '2': ('Guardar en base de datos', accion2),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has elegido la opción 1')
    print("Deseas guardarlo en un csv")

def accion2():
    print('Has elegido la opción 2')
    print("Deseas guardarla en una base de datos")

def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()

    