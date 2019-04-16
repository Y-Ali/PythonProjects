# GoTdict =	{
#     "name": "Arya",
#     "house": "Stark",
#     "age": 20,
#     "sigil": "Direwolf",
#     "alive ?": True,
#     "list_of_names": ["Cersie Lannister", "Ilan Payn", "Sandor Clegain","Sandor Clegain"]
# }
# print(type(GoTdict), "\n")
# print(GoTdict, "\n")
#
# x = GoTdict["name"]
# print(x)
# #changing the name inside the dictionary
# GoTdict["name"] = "girl has no name"
# print(GoTdict["name"],"\n")
#
# #changing an item inside a list, in a dictionary
# GoTdict["list_of_names"][0] = "HELLO"
# print(GoTdict["list_of_names"][0])
# #adding other items to the list in a dictionary
# GoTdict["list_of_names"].append("Yousuf")
# print(GoTdict)
# print(GoTdict["list_of_names"].count("Sandor Clegain"))
#
Storydict =	{
     "name": "1",
     "age": 2,
     "gender": "3",
     "favourite_films": ["not"],
    "occupation": "9"
}
name1= input("What is your name?")
update_name={"name": name1}
Storydict.update(update_name)
#Storydict["name": "1"].update(name1)

age1= int(input("what is your age?: "))
update_age={"age": age1}
Storydict.update(update_age)

gender1 = input("what is your gender? M/F:  ")
count = 0
while count != 1:
    if gender1 == "M" or gender1 == "F" or gender1 == "m" or gender1 == "f":
        update_gender={"gender": gender1}
        Storydict.update(update_gender)
        count = count + 1
    else:
        print("\nplease enter either 'M' or 'F'")
        gender1 = input("what is your gender? M/F:  ")

favourite_films1= input("what are your favourite films?: ")
update_favourite_films={"favourite_films": favourite_films1}
Storydict.update(update_favourite_films)

occupation1= input("what is your occupation?: ")
update_occupation={"occupation": occupation1}
Storydict.update(update_occupation)

print("\nHi", Storydict["name"],"!", "You are", Storydict["age"],"years old, you work as a",Storydict["occupation"],"and your favourite film is", Storydict["favourite_films"])

