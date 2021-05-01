def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #       my_dict[i] = i**3

    # my_list = [1, 2, 3, 4, 5]
    # my_dict = list(map(lambda x: x**2, my_list))

    # print(my_dict)

    # my_list = [2, 2, 2, 2, 2]

    # all_multiplied = 1

    # for i in my_list:
    #     all_multiplied = all_multiplied * i

    #     print(all_multiplied)

    from functools import reduce

    my_list = [2, 2, 2, 2, 2]

    all_multiplied = reduce(lambda a, b: a * b, my_list)

    print(all_multiplied)


if __name__ == '__main__':
    run()
