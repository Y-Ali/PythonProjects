# count = 0
# #while loop
# while count <= 10:
#     print(count)
#     count = count + 1
# print("\n")
# #for loop
# for i in range(10):
#     print(i)

name = ['arya stark','cercei lannister', "theon greyjoy"]
house = ['Stark','Lannister','Greyjoy']
count = 0
number = 1
while count < len(name):
    print(number,"->",name[count].capitalize(),"-> House:", house[count])
    count = count + 1
    number = number + 1
print("\n")

while True:
    user = input("enter something: ")
    if user == "exit":
        print("\nGoodbye...")
        break

    elif user == user.capitalize():
        print("I AM SPARTAAAAA")

    else:
        print("123")
#123455