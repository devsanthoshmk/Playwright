def decor(func):
    def main():
        print("func called")
        func()
        print("done")
    return main

@decor
def first():
    print("inner")
    
first()