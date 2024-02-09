from POO_class import Person

def main():
    new_person = Person(1, "John", 21)
    print(new_person.get_id())
    print(new_person.name)

if __name__ == '__main__':
    main()