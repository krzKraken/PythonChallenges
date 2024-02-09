#!/usr/bin/env python

from rich import print 

print("[bold blue] Reading Files [/bold blue]")
data = ""
with open("hola.txt", "r") as file:
    data = file.read()

print(data);


print("[bold blue] Reading Lines [/bold blue]")

list_lines = []

with open("hola.txt", "r") as f:
    for line in f:
        list_lines.append(line.strip())

print(list_lines)

