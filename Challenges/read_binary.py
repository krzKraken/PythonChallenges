def read_file():
    new_text = []
    with open("file.txt", "r") as file:
        for line in file:
            line.replace("\n", "")
            new_text += line.split(" ")
            print(new_text)
            # print(line)


def main():
    read_file()


if __name__ == "__main__":
    main()