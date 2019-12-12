while True:
    try:
        number = int(input("Enter number: "))
        break
    except ValueError as e:
        print("Input must be an integer")


while True:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1

    print(number)

    if number == 1:
        break
