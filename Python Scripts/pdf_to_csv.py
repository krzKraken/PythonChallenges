import re
import argparse
from pdfreader import PDFDocument, SimplePDFViewer


# Search Patron
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
    # Reading pdf
    file = open("Factura.pdf", "rb")
    viewer = SimplePDFViewer(file)
    viewer.render()
    print(viewer.metadata)
    for canvas in viewer:
        page_text = canvas.text_content

        page_string = canvas.strings

        print(page_string)


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
