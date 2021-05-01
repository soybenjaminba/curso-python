def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    multiplos = [i for i in range(1, 100000) if i % 3 == 0 and if i % 6 == 0 and if i % 9 == 0]

    print(multiplos)


if __name__ == '__main__':
    run()
