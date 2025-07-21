# main.py

from calc import sumar, restar, multiplicar, dividir

def main():
    print("Suma 5 + 3 =", sumar(5, 3))
    print("Resta 5 - 2 =", restar(5, 2))
    print("Multiplicación 4 * 6 =", multiplicar(4, 6))
    print("División 8 / 2 =", dividir(8, 2))

if __name__ == "__main__":
    main()
