import math

radio = float(input("Dime el radio de la de la circunferencia "))

if radio > 0:
    area = math.pi * radio ** 2
    longitud =2 * math.pi * radio
    print(f"Area: {area: .2f} metros cuadrados")
    print(f"Longitud: {longitud: .2f} metros")
else:
    print("Error: el radio de ser mayor que 01")