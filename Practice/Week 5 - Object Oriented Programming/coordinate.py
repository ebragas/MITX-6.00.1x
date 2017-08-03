
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    # Equality method returns True if both coordinates are equal
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False

    # Representation method returns string of function to call to recreate object
    def __repr__(self):
        return "Coordinate(" + str(self.getX()) + "," + str(self.getY()) + ")"

# Testing
c = Coordinate(3, 4)
x = Coordinate(3, 4)
y = Coordinate(4, 3)

print(c == x)
print(x == y)

print(repr(c))
print(repr(y))

z = eval(repr(y))
print(z.getX())
