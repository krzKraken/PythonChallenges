def read_text():
    with open('binarios.txt', 'r') as file:
        lines = file.readlines()
        new_lines = []
        for line in lines:
            new_lines = new_lines + (line.split(' '))
    return new_lines


def clean_data(binary_list):
    my_clean_list = []
    for bin in binary_list:
        my_clean_list.append(str(bin).replace('\n', ''))
    return my_clean_list


def conv_bin_dec(binary_list):
    for bin in binary_list:
        print("Para: ", bin)
        for x, index in enumerate(list(bin)):
            print(x, index)


def main():
    print("main!")
    var = read_text()
    # print(var)
    clean = clean_data(var)
    # print("Clean: ", clean)
    conv_bin_dec(clean)


if __name__ == "__main__":
    main()