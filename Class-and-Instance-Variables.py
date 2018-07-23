"""
Two types of variable example in python:
class variable: like "kind" : define in class, can be used by all instances of the classes
instance variable: like "name" : define by self in init, can be used by unique class "self"
detailed: https://docs.python.org/3/tutorial/classes.html#private-variables
"""
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
