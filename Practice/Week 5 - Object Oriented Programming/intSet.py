
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        # starting with assumption that both sets are equal length
        output = intSet()
        for i in other.vals:
            if self.member(i):
                output.insert(i)
            else:
                pass
        return output

    def __len__(self):
        return len(self.vals)

# Test cases
s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(3)

s2 = intSet()
s2.insert(2)
s2.insert(4)
s2.insert(3)

print(s1.intersect(s2))