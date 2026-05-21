# class animal:
#     def speak(self):
#         print("Animal Speak")

# class Dog(animal):
#     def speak(self):
#         print("Dog Bark")

# dog=Dog()
# dog.speak()

class A:
    def m1(self):
        print("Class A")
class B(A):
    def m2(self):
        print("Class B")
class C(B):
    def m3(self):
        print("Class C")
class D(C):
    def m4(self):
        print("Class D")

obj=D()
obj.m1()
obj.m2()
                        