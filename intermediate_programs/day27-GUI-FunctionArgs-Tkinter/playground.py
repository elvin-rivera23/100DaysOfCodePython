# def add(*numbers):
#     total = sum(numbers)
#     print(total)
#
# add(1,2,3,4)


# ----INSTRUCTOR WAY ----
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1,2,3,4))


# ---- **kwargs ----
def calculate(n, **kwargs):
    print(type(kwargs))     # <class 'dict>
    # print(kwargs)       # {'add': 3, 'multiply': 5}
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])        # will print the value of that key : 3

    n += kwargs["add"]      # 2+3
    n *= kwargs["multiply"] # (2+3)*5

    print(n)    # 25

calculate(2,add=3, multiply=5)  # n=2



class Car:

    def __init__(self, **kw):
        # using get is beneficial, if key doesn't exist in the dictionary it will return NONE and won't give error
        # this is how you create a class with alot of OPTIONAL keyword arguments
        # self.make = kw["make"]
        self.make = kw.get("make")
        # self.model = kw["model"]
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
