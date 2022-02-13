# Showing inheritance
class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
# Instatiating the objects
dad = Parent()
son = Child()
# Calling the implicit function without overriding
dad.implicit()
son.implicit()
# Calling the override function without overriding for Dad object
# while overriding in the son object
dad.override()
son.override()
# Calling the son object before and after using altered()
dad.altered()
son.altered()
print("----------\n" *10)
print('Using Composition now')
# Showing how the same functionality could be applied using composition
class Other(Object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()
# Here it does not override anything as it is not a is-a relationship but instead it is a has-a
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()
