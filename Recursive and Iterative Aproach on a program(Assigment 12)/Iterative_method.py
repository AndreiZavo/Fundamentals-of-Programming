vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def validate(number, difference_allowed_between_numbers):
    index = 0
    ok = True
    for index in range(1, number):
        if vector[number] == vector[index]:
            ok = False
    if index > 0:
        if abs(vector[index + 1] - vector[index]) < difference_allowed_between_numbers:
            return False
    return ok


def show(length_of_string_number):
    for index in range(1, length_of_string_number + 1):
        print(vector[index], end=" ")
    print('')


def back(length_of_string_number, difference_allowed_between_numbers):
    index = 1
    vector[index] = 0
    while index > 0:
        if vector[index] < length_of_string_number:
            vector[index] += 1
            if validate(index, difference_allowed_between_numbers):
                if index == length_of_string_number:
                    show(length_of_string_number)
                    vector[0] += 1
                else:
                    index += 1
                    vector[index] = 0
        else:
            index -= 1
    return vector[0]


def main_itr():
    length_of_string_number = int(input("Please insert the value of n: "))
    difference_allowed_between_numbers = int(input("Please insert the value of m: "))
    number_of_solutions = back(length_of_string_number, difference_allowed_between_numbers)
    if number_of_solutions == 0:
        print("There are no solutions for this values of n and m")

