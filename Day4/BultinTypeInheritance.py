
class Track(list): # here we are extending listclass so it contains list method and attributes also
    def append(self, object):
        print("Append called")

# Create an instance of Track
track = Track()

# Call the append method
track.append("1")


class Track(str):
    def dup(self, other):
        return self + other

t = Track("Python")
print(t.dup(" is awesome"))  # Output: Python is awesome
