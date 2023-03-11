import re
import argparse
import pdfreader as PyPDF2

ruc = "<ruc>"
razon_social = "<razonSocial>"
descripcion_del_gasto = "Descripcion del gasto"
fecha_emision = "<fechaEmision>"
base_12 = "<baseImponible>"
num_autorizacion = "<numeroAutorizacion>"
iva_12 = "<valor>"
propina = "<propina>"
base_0 = ""
forma_pago = "<formaPago>"
total = "<importeTotal>"
punto_emision = "<ptoEmi>"
establecimiento = "<estab>"
secuencia = "<secuencial>"

patron_cedula = r'\d{10}'
patron_ruc = r'\d{13}'
ruc_comprador = "<identificacionComprador>"
fecha_autorizacion = "<fechaAutorizacion>"


def read_pdf():
    # Abrir el archivo PDF en modo de lectura binaria
    with open('Factura.pdf', 'rb') as archivo_pdf:

        # Crear un objeto PDFReader de PyPDF2
        lector_pdf = PyPDF2.PdfFileReader(archivo_pdf)

        # Obtener el número de páginas en el archivo PDF
        num_paginas = lector_pdf.getNumPages()

        # Leer cada página del archivo PDF
        for numero_pagina in range(num_paginas):
            # Obtener la página del PDF
            pagina = lector_pdf.getPage(numero_pagina)

            # Extraer el texto de la página del PDF
            texto_pagina = pagina.extractText()

            # Imprimir el texto de la página
            print(texto_pagina)


def main():
    read_pdf()
    # Crear el objeto ArgumentParser
    parser = argparse.ArgumentParser(
        description='_________Modo de uso________')

    # Agregar los argumentos
    parser.add_argument('-n', '--name', type=str,
                        help='Nombre del archivo "Factura"')
    parser.add_argument('-t', '--type', type=str,
                        help='Tipo de Archivos? [xml/pdf]')

    # Parsear los argumentos
    args = parser.parse_args()

    if args.name:
        print("name: ", args.name)
    if args.type:
        print("type: ", args.type)

    cont = 0
    with open("Factura.xml", 'r') as file:
        for line in file.readlines():
            cont += 1
            if re.search(ruc_comprador, line):
                print("count: ", cont, line)


if __name__ == "__main__":
    main()
// como leer pdf con pdfreader en python?
# PyPDF4 includes a modest (but growing!) test suite built on the unittest
# framework. All tests are located in the tests/ folder and are distributed
# among dedicated modules. Tox makes running all tests over all versions of Python
# quick work:
python - m pip install tox
python - m tox


# Individual tests are accessible as conventional Pytest sources;
pytest - v tests/test_pdf.py


# Source: https://github.com/claird/PyPDF4
