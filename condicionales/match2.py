number = int(input("¿Cuantas pelotas hay?"))

match number:
    case 23:
        print("yes")

    case 78:
        print("nop")

    case 0:
        print("nop")

    case _:
        print("lo siento no adivinaste")


