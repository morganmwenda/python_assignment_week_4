class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person(name="Alice", age=30, gender="Female")
person2 = Person(name="Morgan", age=21, gender="Male")

# Call the introduce method to display the person's information
person1.introduce()
person2.introduce()