import math

def calcular_descuento_entradas(cantidad_entradas):
    """
    Calcula el precio total de las entradas aplicando los descuentos presentado.
    """
    precio_base = 10
    if cantidad_entradas >= 5:
        descuento = 0.25
    elif cantidad_entradas >= 3:
        descuento = 0.15
    else:
        descuento = 0
    precio_final = cantidad_entradas * precio_base * (1 - descuento)
    return precio_final
1
def calcular_area_triangulo_equilatero(lado):
    """
    Calcula el área de un triángulo equilátero dado el lado.
    """
    area = (math.sqrt(3) / 4) * (lado ** 2)
    return area

def mostrar_menu():
    """
    Muestra el menú de opciones y interactua con el usuario.
    """
    while True:
        print("\nMenú de Operaciones:")
        print("1. Calcular descuento por entradas al cine")
        print("2. Calcular área de un triángulo equilátero")
        print("3. Salir del programa")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            try:
                cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))
                if cantidad_entradas < 0:
                    print("La cantidad de entradas no puede ser negativa.")
                else:
                    precio = calcular_descuento_entradas(cantidad_entradas)
                    print(f"El precio total con descuento es: ${precio:.2f}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            try:
                lado = float(input("Ingrese la longitud del lado del triángulo equilátero: "))
                if lado < 0:
                    print("La longitud del lado no puede ser negativa.")
                else:
                    area = calcular_area_triangulo_equilatero(lado)
                    print(f"El área del triángulo equilátero es: {area:.2f}")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    mostrar_menu()
