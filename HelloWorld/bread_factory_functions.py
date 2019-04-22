def dough_maker(water,wheat):
    print(f"mixing {water} with {wheat}")
    if water == "water" and wheat == "wheat":
        return "dough"
    else:
        return "blob"

def bake(something):
    if something == "dough":
        return "this is bread"
    else:
        return "not bread"

def bread_factory(sub1,sub2):
    output = dough_maker(sub1,sub2)
    return bake(output)

##TDD
print(dough_maker("water","wheat"))
print(bake("dough"))

bread_factory("water","flour")

print(bread_factory("water","cement") == "not bread")
print(bread_factory("water", "cement"))



