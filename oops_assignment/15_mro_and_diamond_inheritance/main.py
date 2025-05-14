class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):  # D inherits from both B and C
    pass

# Example usage
obj = D()
obj.show()  # MRO will decide which 'show()' is called
