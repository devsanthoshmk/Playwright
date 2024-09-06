def listing():
    a=0
    while True:
        yield a
        a+=1    
obj=listing()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())