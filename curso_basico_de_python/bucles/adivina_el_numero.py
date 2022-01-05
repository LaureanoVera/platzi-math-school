import random


def run():
    min = 1
    max = 100
    numero_aleatorio = random.randint(min, max)
    numero_usuario = int(input(f"Elige un numero del {min} al {max}: "))
    while numero_usuario != numero_aleatorio:
        if numero_usuario < numero_aleatorio:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_usuario = int(input("Elige otro numero: "))
    print("Ganaste!")


if __name__ == "__main__":
    run()
