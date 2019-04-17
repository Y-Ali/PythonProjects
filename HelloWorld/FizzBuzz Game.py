num = int(input("please enter your starting range: "))
num2 = int(input("please enter your ending range: "))

for i in range (num,num2):
    output = ""     # this will either be Fizz, or Buzz, or Fizzbuzz
    if i % 3 == 0:
        output = output + "Fizz"    # if i is divisible by 3 then output Fizz
    if i % 5 == 0:
        output = output + "Buzz"    # if i is divisible by 5 then output Buzz
    if i % 5 != 0 and i % 3 != 0:
        output = output + str(i)    #if not then output i (a number in the range)
    print(output)
