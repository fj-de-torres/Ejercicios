class Person:
    def set_name(p,name):
        return name

    def greet():
        return f"Hello, my name is {name}."

# Create an instance of Person
p = Person()

# Set the name
p.set_name("Alice")

# Try to greet
print(p.greet())