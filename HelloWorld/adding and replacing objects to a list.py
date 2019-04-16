my_list = ["Tyrion", "Arya", "Sansa"]
print("this is the old list: ", my_list, "\n")

my_list.append("Aegon Targarion")

print("Added 'Aegon Targarion' to the list:", my_list, "\n")

my_list[0] = "The Hound"

print("Replaced Tyrion with 'The Hound': ", my_list)

#adding
my_list[:0] = ["Cersei"]
print("Inserted Cersei to the beginning of the list", my_list)

#using .pop to remove a specific index.
my_list.pop(2)
print (my_list)

