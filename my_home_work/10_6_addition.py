msg = "Type number to sum: "
while True:
    print("If you want to quit, type 'q'")
    num_1 = input(msg)
    num_2 = input(msg)
    if num_1 != 'q' and num_2 != 'q':
        try:
            num_sum = int(num_1) + int(num_2)
        except ValueError:
            print("You need to type integer type . . .\n")
        else:
            print("The sum of two numbers is: " + str(num_sum) + '\n')
    else:
        break
