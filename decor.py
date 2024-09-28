

def greet(fx):
    def modified_fx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return modified_fx

@greet
def hello():
    print("Hello World")

def add(a, b):
    print(a+b)

hello()