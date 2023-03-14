from datetime import date


def saludar(*args):
    for i in args:
        print("Hola -", i)


def despedir(**kwargs):
    for llave, valor in kwargs.items():
        print(f"llave: {llave} y valor: {valor}")


def main():
    today = date.today()
    print("Today:", today)
    saludar("Cristhian", "Joss", "Carlito")
    despedir(gerente="Cristhian", subgerente="Joss", presidente="Carlitos")


if __name__ == "__main__":
    main()
