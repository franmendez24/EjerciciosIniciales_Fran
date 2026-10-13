def numero_a_romano(num):
    """
    Convierte un número entero a su representación en numeración romana.

    Recibe:
    num (int): número entero a convertir.

    Devuelve:
    str: el numeral romano correspondiente, o el texto
    "Número inválido. Debe estar entre 1 y 3999." si el número
     está fuera del rango válido.
    """
    if num < 1 or num > 3999:
        return "Número inválido. Debe estar entre 1 y 3999."

    pares = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]

    resultado = ""
    for valor, simbolo in pares:
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado

try:
    numero = int(input("Introduce un número entero: "))
    print(numero_a_romano(numero))
except ValueError:
    print("Entrada inválida. Debe ser un número entero.")