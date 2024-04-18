def area_rectangulo(a, b):
    result = a * b
    return result

def area_triangulo(b, h):
    r = 0.5 * b * h
    return r

def principal():
    x = 4
    y = 6
    print(f"Área del rectángulo: {area_rectangulo(x, y)}")

    base = 5
    altura = 8
    print("Área del triángulo:", area_triangulo(base, altura))

principal()
