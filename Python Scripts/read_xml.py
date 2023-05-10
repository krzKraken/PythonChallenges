import os
import re
from enum import Enum

xml_list = []
factura_list = []
total_sin_impuestos=''
total_iva_12=''
# Class factura
class Factura:
    
    def __init__(self, ruc_proveedor='9999999999', razon_social='razon Social', descripcion_gasto='Descripcion de gasto', fecha_emision ='Fecha de emision', subtotal_12='0', base_0='0', propina='0', iva_12='0', total='0', numero_autorizacion='0', punto_emision='999', establecimiento='999', sec_factura='999999999', tipo_documento='0', forma_pago='0'):
        self.ruc_proveedor = ruc_proveedor
        self.razon_social = razon_social
        self.descripcion_gasto = descripcion_gasto
        self.fecha_emision = fecha_emision
        self.subtotal_12 = subtotal_12
        self.propina = propina
        self.base_0 = base_0
        self.iva_12 = iva_12
        self.total = total
        self.numero_autorizacion = numero_autorizacion
        self.punto_emision = punto_emision
        self.establecimiento = establecimiento
        self.sec_factura = sec_factura
        self.tipo_documento = tipo_documento
        self.forma_pago = forma_pago
    def __str__(self):
        return str(self.__dict__)

# create a enum with each factura field
class FacturaEnum(Enum):
    ruc_proveedor = '<ruc>'
    razon_social = '<razonSocial>'
    descripcion_gasto = '<descripcionGasto>'
    fecha_emision = '<fechaEmision>'
    subtotal_12 = '<baseImponible>'
    propina = '<propina>'
    base_0 = '<>'
    iva_12 = '<valor>'
    total = '<importeTotal>'
    numero_autorizacion = '<numeroAutorizacion>'
    punto_emision = '<ptoEmi>'
    establecimiento = '<estab>'
    sec_factura = '<secuencial>'
    tipo_documento = '<codDoc>'
    forma_pago = '<formaPago>'


def list_xml_files():
    for file in os.listdir("."):
            if file.endswith(".xml"):
                print(file)
                xml_list.append(str(file))

# read xml files with python
def read_xml():
    # todo: for factura in lista de facturas 
    with open("/home/krzkraken/Desktop/PythonChallenges/Python Scripts/Factura.xml","r") as xml:
        my_factura = Factura()
        
        for line in xml:

            #* Getting numero autorizacion
            if str(line).__contains__(FacturaEnum.numero_autorizacion.value):
                res = re.search(r"\d+", str(line))
                if res is not None:
                    my_factura.numero_autorizacion = str(res.group(0))   
                else:
                    my_factura.numero_autorizacion = '-- Autorizacion --'

            #* Getting razon Social
            if str(line).__contains__(FacturaEnum.razon_social.value):
                res = re.search(r"<razonSocial>(.*?)</razonSocial>", str(line))
                if res is not None:
                    my_factura.razon_social = res.group(1)
                else:
                    my_factura.razon_social = 'razon Social'
            
            #* Getting RUC number
            if str(line).__contains__(FacturaEnum.ruc_proveedor.value):
                res = re.search(r"\d{13}",str(line))
                if res is not None:
                    my_factura.ruc_proveedor = res.group(0)
                else:
                    my_factura.ruc_proveedor = '9999999999'

            #* Getting stablisetment number
            if str(line).__contains__(FacturaEnum.establecimiento.value):
                res = re.search(r"\d{3}", str(line))
                if res is not None:
                    my_factura.establecimiento = res.group(0)
                else:
                    my_factura.establecimiento = '--Establecimiento--'
            #* Getting emision point
            if str(line).__contains__(FacturaEnum.punto_emision.value):
                res = re.search(r"\d{3}", str(line))
                if res is not None:
                    my_factura.punto_emision = res.group(0)
                else:
                    my_factura.punto_emision = '--Punto de emision--'
            #* Obteniendo secuencia
            if str(line).__contains__(FacturaEnum.sec_factura.value):
                res = re.search(r"\d{9}", str(line))
                if res is not None:
                    my_factura.sec_factura = res.group(0)
                else:
                    my_factura.sec_factura = '--Secuencia Factura--'

            #* Getting emition date
            if str(line).__contains__(FacturaEnum.fecha_emision.value):
                res = re.search(r"\d{2}\/\d{2}\/\d{4}", str(line))
                if res is not None:
                    my_factura.fecha_emision = res.group(0)
                else:
                    my_factura.fecha_emision = '--fecha de emision--'


            #* Getting description
            if str(line).__contains__(FacturaEnum.descripcion_gasto.value):
                #TODO: This should return [food, gasoline, transport, hotel, etc.]

                res = re.search(r"<descripcionGasto>(.*?)</descripcionGasto>", str(line))
                if res is not None:
                    my_factura.descripcion_gasto = res.group(1)
                else: 
                    my_factura.descripcion_gasto = '--Descripcion de gasto--'
         
            #* Getting Total without taxes
            if str(line).__contains__(FacturaEnum.subtotal_12.value):
                res = re.search(r"<baseImponible>(\d+\.\d+)</baseImponible>", str(line))                
                global total_sin_impuestos

                if res is not None and total_sin_impuestos =='':
                    my_factura.subtotal_12 = res.group(1)
                    total_sin_impuestos=res.group(1)
                else:
                    my_factura.subtotal_12 = '--total sin impuestos--'
                    
            #* Getting tips
            if str(line).__contains__(FacturaEnum.propina.value):
                res = re.search(r"<propina>(\d+\.\d+)</propina>", str(line))
                if res is not None:
                    my_factura.propina = res.group(1)
                else:
                    my_factura.propina = '--propina--'
            
            #* Getting base 0%
            if str(line).__contains__(FacturaEnum.base_0.value):
                res = re.search(r"<codigoPorcentaje>0</codigoPorcentaje><baseImponible>(\d+\.\d+)</baseImponible>", str(line))
                if res is not None:
                    my_factura.base_0 = res.group(1)
            
            #* Getting IVA 12%
            if str(line).__contains__(FacturaEnum.iva_12.value):
                res = re.search(r"<valor>(\d+\.\d+)</valor>", str(line))
                if res is not None:
                    my_factura.iva_12 = res.group(1)
                else:
                    my_factura.iva_12 = '--iba 12%--'
            if str(line).__contains__(FacturaEnum.total.value):
                res = re.search(r"<importeTotal>2(\d+\.\d+)</importeTotal>", str(line))
                if res is not None:
                    my_factura.total = res.group(1)
                else:
                    my_factura.total = '--total--'
                my_factura.total = str(line)
            if str(line).__contains__(FacturaEnum.tipo_documento.value):
                #TODO: Get tipo documento
                print(line)
                my_factura.tipo_documento = str(line)
            if str(line).__contains__(FacturaEnum.forma_pago.value):
                #TODO: Get forma pago
                print(line)
                my_factura.forma_pago = str(line)
    print(my_factura.__str__())



def main():

    list_xml_files()
    print(xml_list)
    read_xml()

if __name__=="__main__":
    main()