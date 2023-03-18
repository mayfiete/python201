
# nested function
def thing1():
    print("hey")

    def thing2():
        print("hey hey")
    thing2()
    # a decorator is a function within a function


thing1()
