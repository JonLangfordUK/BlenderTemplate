""" Example Classes being used in other modules. """


class Animal:
    """
    A class representing an animal with basic attributes and behaviors.
    This class provides a foundation for creating animal objects with properties
    like name, age, and mood, along with basic animal behaviors.
    Attributes:
        name (str): The name of the animal.
        age (int): The age of the animal in years.
        mood (str): The current mood/emotional state of the animal.
    Methods:
        speak(): Returns a string representing the sound the animal makes.
    """

    def __init__(self):
        """
        Initializes a new Animal object with default attributes.
        """

        self.name = ""
        self.age = 0
        self.mood = ""
    
    def speak(self) -> str:
        """
        Default functionality to allow child Animals to speak.
        Returns:
            str
        """

        return ""


class Dog(Animal):
    """A class representing a dog, inheriting from Animal.
    This class implements a basic dog with attributes for name, age, and mood,
    and includes a method for the dog's speech sound.
    Attributes:
        name (str): The name of the dog, defaults to "Elsie"
        age (int): The age of the dog in years, defaults to 8
        mood (str): The current mood of the dog, defaults to "Happy"
    Methods:
        speak(): Returns the dog's bark sound
    """

    def __init__(self):
        """
        Initializes a new Dog object with default attributes.
        """

        self.name = "Elsie"
        self.age = 8
        self.mood = "Happy"

    def speak(self) -> str:
        """
        Allows the Dog to vocalize with a "Woof!" sound.
        Returns:
            str
        """

        return "Woof!"


class Cat(Animal):
    """A class representing a Cat, inheriting from Animal.
    This class defines a basic cat with attributes for name, age, and mood,
    and implements a speak method for cat vocalization.
    Attributes:
        name (str): The name of the cat, defaults to "Penelope"
        age (int): The age of the cat in years, defaults to 5
        mood (str): The current mood of the cat, defaults to "Grumpy"
    Methods:
        speak(): Makes the cat vocalize with a "Meow!"
    Inherits from:
        Animal
    """

    def __init__(self):
        """
        Initializes a new Cat object with default attributes.
        """

        self.name = "Penelope"
        self.age = 5
        self.mood = "Grumpy"

    def speak(self) -> str:
        """
        Allows the cat to vocalize with a "Meow!" sound.
        Returns:
            str
        """

        return "Meow!"
