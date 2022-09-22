import copy
class Singleton():
    def __new__(cls):
        return cls

    @staticmethod
    def static_method():
        #use this if no inner variables required
        pass

    @classmethod
    def class_method(cls):
        #use this if class variables needs to be accessed
        pass

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")
OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")
OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")
OBJECT3 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT3)}")