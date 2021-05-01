def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    super_list = [
        {"firstaname": "Facundo", "lastname": "García"},
        {"firstaname": "Miguel", "lastname": "Torres"},
        {"firstaname": "Pepe", "lastname": "Rodelo"},
        {"firstaname": "Susana", "lastname": "Martínez"},
        {"firstaname": "José", "lastname": "García"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()
