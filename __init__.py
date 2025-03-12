""" Basic example of a Blender Addon using a register and unregister function. """

from src.example_class import Animal, Dog, Cat

def register():
    """
    Example of a basic register function for a Blender Addon.
    """
    animal_a: Animal = Dog()
    animal_b: Animal = Cat()

    print("Registering Blender Addon")

def unregister():
    """
    Example of a basic unregister function for a Blender Addon.
    """
    print("Unregistering Blender Addon")