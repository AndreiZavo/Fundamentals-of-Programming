vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def valid(number, difference_allowed_between_numbers):
    for index in range(1, number):
        if vector[number] == vector[index]:
            return False
        if number > 1:
            if abs(vector[number] - vector[number - 1]) < difference_allowed_between_numbers:
                return False
    return True


def back(number, length_of_string, difference_allowed_between_numbers):
    for index_i in range(1, length_of_string + 1):
        vector[number] = index_i
        if valid(number, difference_allowed_between_numbers):
            if number == length_of_string:
                vector[0] += 1
                for index_j in range(1, length_of_string + 1):
                    print(vector[index_j], end=" ")
                print("")
            else:
                back(number + 1, length_of_string, difference_allowed_between_numbers)
    return vector[0]


def main_rcv():
    length_of_string = int(input("Please insert the value of n: "))
    difference_allowed_between_numbers = int(input("Please insert the value of m: "))
    number_of_solutions = back(1, length_of_string, difference_allowed_between_numbers)
    if number_of_solutions == 0:
        print("There are no solutions for this values of n and m")
