""" Basic example of a Blender Addon using a register and unregister function. """

## ERROR - This is not working, the classes are not being imported
#from src.example_class import Animal, Dog, Cat

def register():
    """
    Example of a basic register function for a Blender Addon.
    """
    #animal_a: Animal = Dog()
    #animal_b: Animal = Cat()

    print(f'Registering {__name__.split(".")[-1]} addon')
    

def unregister():
    """
    Example of a basic unregister function for a Blender Addon.
    """
    print(f'Unregistering {__name__.split(".")[-1]} addon')