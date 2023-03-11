def main():
    my_dict = {
        "name": "Cristhian",
        "age":  31,
        "weight": "85 Kg"
    }
    print(my_dict)
    print("__________Add keys_________")
    my_dict.update({
        "size": 167
    })
    print(my_dict)
    print("____________Dict inside Dict___________")
    my_dict["saludo"] = ({
        "hola": "buenos dias",
        "chao": "Buenas noches"
    })
    print(my_dict)
    print("_________reading dict inside dict________")
    print(f'{my_dict["name"]} {my_dict["saludo"]["hola"]} ')
    print("___________Printing keys_________")
    print(my_dict.keys())
    values = my_dict.values()
    print(values)
    print("Values in for")
    for i in values:
        print(i)


if __name__ == "__main__":
    main()
