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





