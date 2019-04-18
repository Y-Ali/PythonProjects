def making_bread():
    print("we will make some bread")


def full_name1(f_name,l_name):
    full_name_b = (f_name + " " + l_name)
    return full_name_b

print(full_name1("yousuf","ali"))


def find_area(radius):              #define a function, find_area with a radius being passed in as an argument
    pi = 3.14
    area = pi*(radius*radius)       #calculation for the area of a circle
    return area
print(find_area(10))                #radius = 10
#find_area(10)

def find_area(radius,pi = 3.14):              #define a function, find_area with a radius being passed in as an argument
    #pi = 3.14
    #area = pi*(radius*radius)       #calculation for the area of a circle
    return pi* radius*radius
print(find_area(25))

def uppercase(string):
    return string.upper()
print(uppercase("hello"))


def full_name(f_name,l_name,middle_n = ""): #this function shows that you have the choice of 2 names being printed
    # if middle_n == "Snow":                # or 3 names. the code will still work.
    return f"{f_name} {middle_n} {l_name}"

print(full_name("Yousuf","ali"))




