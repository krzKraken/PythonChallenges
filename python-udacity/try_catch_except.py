#!/usr/bin/env python

from rich import print

# try catch except 

while True:
    try:
        x = int(input("Ingrese un numero de Galletas: "))
        y = int(input("Ingrese un numero de personas "))
        porcion = x/y
        print("La porcion de galletas es: ",porcion)
        break
    except ZeroDivisionError as e :
        print( "ZerroDivisionError: {}\n".format(e))
    except KeyboardInterrupt as k:
        print("\n[bold red]\n Saliendo... [/bold red]")
        break
    finally:
        print("\n[bold green] ... Finally... [/bold green]")
    