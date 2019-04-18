def dough(water,wheat):
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

print(dough("water","wheat"))
print(bake("dough"))


def bread_factory(sub1,sub2):
    output = dough(sub1,sub2)
    return bake(output)

bread_factory("water","flour")

print(bread_factory("water","cement") == "not bread")
print(bread_factory("water", "cement"))