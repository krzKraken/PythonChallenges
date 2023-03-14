def main():
    text = "hola, {}".format("Cristhian")
    text = """ Esto es un {0} para el que quiera recibir el {0}  y sino para ti {1}""".format(
        "mensaje", "Cristhian"
    )
    text = """Esto es un print con {par} que tienen {nom}""".format(
        par="Parametros", nom="Nombrados"
    )

    print(text)


if __name__ == "__main__":
    main()
