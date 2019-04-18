accounts = {1: {"name": "Arya ", "money": "£100000000 "},
            2: {"name": "Bob the Builder", "money": "£1000"},
            3: {"name": "Spongebob ", "money": "£5000"}
            }

#print(accounts.values())
# print(accounts[1]) ### this will output the key 1 dictionary.
# print(accounts[1]["name"]) ## this will output the name in key 1
#
#
# print("\n")
#
# for i in accounts:
#     values = accounts[i]
#     print(values)
# print("\n")

for each_account_dictionary in accounts.values():  #for every item in accounts, output the values {}
    print("the embedded dictionary: ",each_account_dictionary)
    for embedded_val in each_account_dictionary.values(): # for each item (the values) output them individually
        print(embedded_val)

# for key in accounts:
#     for embedded_val in accounts[key]:
#         print(accounts[key][embedded_val])





