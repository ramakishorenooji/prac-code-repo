# simple_generator.py

def simplegenerator():
    yield 1
    yield 2
    yield 3


x = simplegenerator()

print(x.__next__())
print(x.__next__())
print(x.__next__())
