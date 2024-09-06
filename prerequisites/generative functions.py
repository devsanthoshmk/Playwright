def listing():
    yield 1
    yield 2
    yield 3
    yield 3
    yield 3
    yield 3
obj=listing()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())