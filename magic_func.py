import matplotlib as mpl


class Myclass():
    def __init__(self):
        pass

    def __repr__(self):
        print("this is modified repr")
    def show(self):
        print("test class")

myclass = Myclass()
myclass.show()

print()

print(myclass.__dict__)
print(myclass.__class__)
print(myclass.__dir__())
print(myclass.__repr__())