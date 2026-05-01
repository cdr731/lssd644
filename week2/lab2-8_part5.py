# Lab 2-8 Part 5 by Chris Reutz

# define a class called 'Box'
class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        return (self.length * self.width * self.height)

# create a 'mybox' object using the 'Box' class
mybox = Box(7, 2, 4)
print(f'My box is {mybox.length} units by {mybox.width} units by {mybox.height} units.')
print(f'It has a volume of {mybox.volume()} units.')

# create an instance variable of my 'name' for mybox
mybox.name = 'Chris'
print(f'My box\'s name is {mybox.name}, which happens to be my name!')