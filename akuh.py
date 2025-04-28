class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My Name is: {self.name} and i am {self.age} years old."

    def greeting(self):
        user = input("Enter You Name: ")
        return f"Hello, {user} How are you doing today"


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your Age: "))

    person = Person(name, age)
    print(person)
    print()
    print(person.greeting())


if __name__ == "__main__":
    main()
