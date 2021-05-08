local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"



if __name__ == "__main__":
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())

    print(__name__)
    print("the file is being executed directly") #any code inside the main will not be executed in the child.
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__) #this is what will be executed or appear in the child file.
  