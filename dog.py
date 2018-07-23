###### PART 1 ######
class Things():
	pass
class Living(Things):
	pass
class Animals(Living):
	pass
	
class Dog(Animals):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


some_dog = Dog('koa', 3)
my_dog = Dog('shandy', 7)


###### PART 2 ######
# Put your dog's (or an imaginary dog) info below:
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("\n")


###### END PART 2 ######

print("My dog's name is " + some_dog.name.title() + ".")
print("My dog is " + str(some_dog.age) + " years old.")
print("\n")

some_dog.sit()
some_dog.roll_over()

print("\n")

###### PART 3 ######
# Tell your dog to sit and roll over:
my_dog.sit()
my_dog.roll_over()

print("\n")


###### END PART 3 ######
