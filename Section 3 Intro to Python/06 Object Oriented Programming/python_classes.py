class MyClass:
    a = 5
    print("Hello")

    def hello(self):        # self is required to instantiate the method
        print("Hello World!")

myc= MyClass()
print(myc.a)
print(myc.hello())