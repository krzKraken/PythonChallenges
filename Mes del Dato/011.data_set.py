# Status, Valencia, Borka
# Todas las rutas abiertas, 1, 1
# Todas las rutas cerradas, 0, 0

# Paso 1: Crea una funcion para poder leer el archivo status.txt y generar una lista con los datos

# Paso 2: Crea otra function para normalizar los datos de la lista

# Paso 3: Crea otra function para identificar si las rutas estan abiertas o cerradas

# Paso 4: Crea otra function para generar el archivo csv con los datos normalizados

import csv


def identify_routes(my_file):
    # status, Valencia, Borka
    response = []

    for status in my_file:
        if "las rutas estan abiertas" in status:
            response.append([status, 1, 1])
        elif "las rutas de valenciana y borja estan abiertas" in status:
            response.append([status, 1, 1])
        elif "las rutas de borja y valenciana estan abiertas" in status:
            response.append([status, 1, 1])
        elif "las rutas en valenciana estan abiertas" in status:
            response.append([status, 1, 0])
        elif "las rutas estan abiertas" in status:
            response.append([status, 1, 1])
        elif "todas las rutas estan abiertas" in status:
            response.append([status, 1, 1])
        elif "todas las rutas estan cerradas" in status:
            response.append([status, 0, 0])
        elif "borja esta abierta" in status and "valencia esta abierta" in status:
            response.append([status, 1, 1])
        elif "borja esta cerrada" in status and "valencia esta abierta" in status:
            response.append([status, 1, 0])
        elif "borja esta abierta" in status and "valencia esta cerrada" in status:
            response.append([status, 1, 0])
        elif "borja esta cerrada" in status and "valencia esta cerrada" in status:
            response.append([status, 0, 0])
        elif "borja estan abiertas" in status and "valencia estan abierta" in status:
            response.append([status, 1, 1])
        elif "borja estan cerradas" in status and "valencia estan abierta" in status:
            response.append([status, 1, 0])
        elif "borja estan abiertas" in status and "valencia estan cerradas" in status:
            response.append([status, 1, 0])
        elif "borja estan cerradas" in status and "valencia estan cerradas" in status:
            response.append([status, 0, 0])
        elif "borja esta abierta" in status:
            response.append([status, 0, 1])
        elif "borja estan abiertas" in status:
            response.append([status, 0, 1])
        elif "valenciana estan abiertas" in status:
            response.append([status, 1, 0])
        elif (
            "las rutas de valenciana estan abiertas" in status
            and "borja estan abiertas" in status
        ):
            response.append([status, 1, 1])
        elif (
            "los demas senderos estan abiertos" in status and "valenciana" not in status
        ):
            response.append([status, 1, 0])
        elif "los demas senderos estan abiertos" in status and "borja" not in status:
            response.append([status, 0, 1])
        elif (
            "los demas senderos estan abiertos" in status
            and "borja" not in status
            and "valenciana" not in status
        ):
            response.append([status, 0, 1])
        else:
            response.append([status, -1, -1])
    return response


def remove_duplicated(my_file):
    my_new_text = set(my_file)
    my_new_text = list(my_new_text)
    return my_new_text


def all_to_lower_case(my_file):
    my_new_text = []
    with open(str(my_file), "r") as file:
        for line in file:
            new_line = (
                line.lower()
                .replace("ã¡", "a")
                .replace("ã©", "e")
                .replace("ã­", "i")
                .replace("ã³", "o")
                .replace("ãº", "u")
                .replace("!", "")
                .replace("?", "")
                .replace('"', "")
                .replace(".", "")
                .replace(",", "")
                .replace("(", "")
                .replace(")", "")
                .replace("@", "a")
                .replace("â¡", "")
                .replace("â¿", "")
            )
            my_new_text.append(new_line.strip())
            # my_new_text.append(line.strip())
    return my_new_text


def create_csv(my_file):
    with open("status.csv", "w") as file:
        headers = ["Status", "Valenciana", "Borja"]
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(identify_routes(my_file=my_file))


def main():
    text = all_to_lower_case("status.txt")
    text = remove_duplicated(text)
    # text = identify_routes(text)
    create_csv(text)
    # con = 0
    # for i in text:
    #     con += 1
    #     print(con, i)


if __name__ == "__main__":
    main()
