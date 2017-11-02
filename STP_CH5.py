# METHODS
# Like functions. For classes of data
ex = "Hello".upper()
print(ex)

ex = "Hello".replace("o","@")
print(ex)

# LISTS. CONTAINERS THAT MUTABLE, ITERABLE, AND STORE OBJECTS IN A SPECIFIC ORDER
def print_list(fruit):
    """
    Print the list of items
    :param fruit: list
    :return: none
    """
    for i in range (len(fruit)):
        print(fruit[i])

fruit = list()
print(fruit)
print("-----------------append fruit list-------------------")
fruit = ["orange", "banana", "pear"]
fruit.append("apple")
fruit.append("peach")
print_list(fruit)
print("-----------------pop fruit list-------------------")
fruit.pop()
print_list(fruit)
print("-----------------check fruit list-------------------")
isit = "orange" in fruit
print(isit)
isitnot = "orange" not in fruit
print(isitnot)

#TUPLES: IMMUTABLE LISTS. SPECIFIC ORDER, ITERABLE
oldlady = tuple()
print(oldlady)
oldlady = ("Miss Jackson", "Apology", True, 1000,)
print(oldlady)
print(len(oldlady))
print_list(oldlady)

#DICTRIONARIES LINE A KEY TO AN VALUE. MAPPING INO KEY-VALUE PAIRS
#MUTABLE, NO SPECIFIC ORDER
print("-----------------dictionaries-------------------")
my_dict = dict()
my_dict = {}
print(my_dict)
my_dict["double feature screen"] = "straight to dvd"
my_dict["bigger than a bridge"] = "look like a little kid's"
my_dict["locked in a cage, right"] = "suffer from stage fright"
my_dict["so hot, it's stolen"] = "look like Gary Coleman"
print(my_dict["double feature screen"])
isit = "so hot, it's stolen" in my_dict
print(isit)









