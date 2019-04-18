import random
# # print a formated list of movies:
# movies_list = ["Narnia", "Iron Man","Avengers: Infinity War", "Star Wars", "Inception"]
# number = 1
# print("List of movies: ")
# for item in movies_list:
#     print(number,"-", item.capitalize())
#     number = number + 1
# print("my favourite movie is", movies_list[2])
# print("\n")
#
# #print a formated list of places to visit
# print("List of places: ")
# places_list = ["Egypt", "Japan", "Italy", "Turkey", "Brazil"]
# number_1 = 1
# for item in movies_list:
#     print(number_1, "-", item.capitalize())
#     number_1 = number_1 + 1
#
# print("\n")
#
# #outputing the values from the dictionary
# my_dictionary = {1:{"movies": ["Narnia", "Iron Man","Avengers: Infinity War", "Star Wars", "Inception"]},
#                 2:{"places": ["Egypt", "Japan", "Italy", "Turkey", "Brazil"]}
# }
# for item in my_dictionary:
#     values = my_dictionary[item]
#     print(values)
# print("\n")

#####magic number game (the 'list' version) - not complete!!!!
# number_of_goes = 3
# attempt = 1
# index = 0
# the_magic_num_is = 4
# magic_number_list = [1,2,3,4,5,6]
# while number_of_goes <= 3:
#     print("Try and guess the magic number.","attempt",attempt)
#     user_input = int(input("Guess: "))
#     for item in magic_number_list:
#         if user_input == magic_number_list[index]:
#             number_of_goes = number_of_goes + 3
#             print("Well Done! The magic number was", the_magic_num_is)
#             break
#         elif user_input != magic_number_list[index]:
#             print("Oops, that's wrong!\n")
#             number_of_goes = number_of_goes - 1
#             attempt = attempt + 1
#             index = index + 1
#             print("Number of goes remaining: ", number_of_goes)
#
#             if number_of_goes == 0:
#                 print("Sorry, you've had enough attempts! The magic number was:", )
#                 break
#         else:
#             print("lalalalalala!")

#magic number game (the 'random number' version)
def game():         #defining 'game' function
    number_of_goes = 3
    attempt = 1
    random_magic_number_generator = random.randrange(1,6)
    while number_of_goes <= 3:
        #print("The number is:",random_magic_number_generator)
        print("\nTry and guess the magic number.","attempt",attempt)
        #print(random_magic_number_generator)

        user_input = int(input("Guess: "))
        if user_input == random_magic_number_generator:
            number_of_goes = number_of_goes + 3
            print("Well Done! The magic number was", random_magic_number_generator)
            play_again()
            break

        elif user_input != random_magic_number_generator:
            print("Oops, that's wrong!\n")
            number_of_goes = number_of_goes - 1
            attempt = attempt + 1
            print("Number of goes remaining: ", number_of_goes)

            if number_of_goes == 0:
                print("Sorry, you've had enough attempts! The magic number was:", random_magic_number_generator)
                break
        else:
            print("That's not a number!")

def play_again():
    yes_no = input("\nPlay again?: ")
    if yes_no == "y":
        game()
    elif yes_no == "n":
        print("\nGoodbye...!")
game()