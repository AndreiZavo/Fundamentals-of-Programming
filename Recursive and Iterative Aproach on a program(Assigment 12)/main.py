from Iterative_method import main_itr
from recursive_method import main_rcv


def run():
    while True:
        choice = input("Choose the type of implementation of the algorithm you want: ")
        if choice == '1':
            main_itr()
        elif choice == '2':
            main_rcv()
        else:
            return
run()