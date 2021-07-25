print("Give me two numbers, and I'll divide them.")
print("Enter 'q' ti quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:                # - Если try выполнен успешно, except - пропускается.
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:      # Как следует поступать при возникновении ошибки ZeroDivisionError
        print("You can't divide by 0!")  # Вместо ошибки выполняет код.
    else:                                        # Если try: - успешно, то код продолжается в else:
        print(answer)
