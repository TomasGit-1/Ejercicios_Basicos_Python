"""
    Python Object Oriented Programming 
    python is a multi-paradigm programming language. it supports differente 
    programming approaches.

    One of the popular approaches to solve a programming problem is by creating 
    objects. This is known as object-oriented-programming (POO)
"""

class Parrot:

    #class attribute
    species = "bird"

    def __init__(self, name , age):
        self.name = name
        self.age = age

# Instantiate the parrot class
blu = Parrot("Blu" , 10)
woo = Parrot("Woo" , 15)

#Access the class attributes
print("Blue is as {}".format(blu.__class__.species))
print("Woo is also a  {}".format(woo.__class__.species))


# # Access the instance attributes
print("{} is {} years old".format(blu.name , blu.age))
print("{} is {} years old".format(woo.name , woo.age))