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

# Challenge 1. Make a list of musicioans
myMusic = ["21 Pilots", "Lumineers", "Mumford and Sons"]
print_list(myMusic)

# Challenge 2. Create  a list of Tuples of cities.
Denver = (39.7392, 104.9903)
Atlanta = (33.7490, 84.3880)
London = (51.5074, 0.1278)
myCities = [Atlanta, Denver, London]
print_list(myCities)

#Challenge 3. Create a dictionary
superSize = dict()
superSize["age"] = 44
superSize["height"] = 80
superSize["weight"] = 300
superSize["hair"] = "red"
print(superSize["age"])

#Challenge 6. What is a set?
# Sets are unordered collections of items. Each element is unique and immutable.
# The set is mutable. The elements are not.
myset = {1,2,3,4,3,2,1}
print(myset)  #duplicates will drop out







