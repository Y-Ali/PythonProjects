

age = int(input("What is your age?: "))
if age < 18:
    print("Sorry, you not old enough to drive!\n")

elif age >=18:

    driver_licence = input("Do you have a drivers licence?: (Y/N)")

    if age >= 18 and driver_licence == "y":
            print("You can drive!\n")


    elif age >= 18 and driver_licence == "n":
        print("You are old enough to drive, but do not have a driving licence!\n")

    else:
        print("Sorry, you not old enough to drive!\n")



age = int(input("what is your age?: "))
movie_rating = input("what is the movie rating?: if you dont know, please click the space bar.")

if movie_rating == " ":
    if age >= 0 and age <=11:
        print("According to your age, you can watch the following rated films: PG")

    elif age >= 12 and age < 15:
        print("According to your age, you can watch the following rated films: PG and 12")

    elif age >= 15 and age <18:
        print("According to your age, you can watch the following rated films: PG, 12, and 15")

    else:
        print("you can watch any rated film!")


