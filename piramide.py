# funcion que crea la piramide en funcion del numero del input
def generar_piramide(n):
    for i in range(1, n + 1):
        espacios = " " * (n - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

# funcion que comprueba si el input es correcto o no (que sea un numero y mayor que 1)
def comprobar_input():
    while True:
            n = int(input("Ingrese un número entero mayor o igual a 1: "))
            if n >= 1:
                generar_piramide(n)
                break
            else:
                print("El número debe ser mayor o igual a 1. Inténtelo nuevamente.")

if __name__ == "__main__":
    comprobar_input()