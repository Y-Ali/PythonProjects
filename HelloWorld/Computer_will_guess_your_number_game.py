import random
def starting():
    user_input = input("\ndo you want to play a game? Y/N ")
    if user_input == "Y" or user_input == "y":
        start_game()
    else:
        print("Goodbye..!")

def start_game():
    print("i will try to guess your number\n")
    random_number_to_add_later = random.randrange(1,500)

    computer_number = random.randrange(1,100)
    computer_double = computer_number * 2
    computer_add =  computer_double + random_number_to_add_later
    computer_half = computer_add / 2
    computer_subtract = computer_half - computer_number

    user_think_of_num = input("Think of a number...type y when done: ")
    user_double_it = input("\ndouble your number, please type y when done: " )

    print("\nadd", random_number_to_add_later, "with your current number.")
    add_number = input("\nplease type y when done: ")

    half_number = input("\nhalf your current number. please type y when done: ")
    subtract_number = input("\nsubtract your current number with the number you started with. please type y when done: ")

    print("\nis your number", computer_subtract,"?" )
    am_i_correct = input("y/n: ")
    if am_i_correct == "y":
        print("\nI am a genius.\n")
    else:
        print("you win!")
    play_again()

def play_again():
    again = input("do you want to play again? y/n: ")
    if again == "y":
        starting()
    else:
        print("Goodbye...!")

starting()