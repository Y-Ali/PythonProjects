accounts = {1: {"name": "Arya ", "money": "£100000000 "},
            2: {"name": "Bob the Builder", "money": "£1000"},
            3: {"name": "Spongebob ", "money": "£5000"}
            }
for obj in accounts.values():
    print(obj) #this will output the dictionary for each key
    print(obj.values()) #this will basically create (but not create) a list)

    print("\n")
    for something in obj.values(): #for each item in the new list (but not a list) it will output each value
        print(something)