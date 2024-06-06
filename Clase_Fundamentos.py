def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_digitos(num):
    return sum(int(digit) for digit in str(num))

def producto_digitos(num1, num2):
    return num1 * num2

def mostrar_digitos_separados(num1, num2):
    return list(str(num1)) + list(str(num2))

def main():
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    diferencia = abs(num1 - num2)

    if diferencia % 2 == 0:
        suma = suma_digitos(num1) + suma_digitos(num2)
        print("La suma de los dígitos de los números es:", suma)
    elif es_primo(diferencia) and diferencia < 10:
        producto = producto_digitos(num1, num2)
        print("El producto de los dos números es:", producto)
    elif str(diferencia).endswith('4'):
        digitos_separados = mostrar_digitos_separados(num1, num2)
        print("Los dígitos de los números por separado son:", ' '.join(digitos_separados))

if __name__ == "__main__":
    main()
