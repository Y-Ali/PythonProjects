my_list = ["Tyrion", "Arya", "Sansa"]
print("this is the old list: ", my_list, "\n")

my_list.append("Aegon Targarion")

print("Added 'Aegon Targarion' to the list:", my_list, "\n")

my_list[0] = "The Hound"

print("Replaced Tyrion with 'The Hound': ", my_list)

my_list[:0] = ["helloooo"]
print(my_list)

