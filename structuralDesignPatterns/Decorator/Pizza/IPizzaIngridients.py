from zope.interface import Interface


class IPizzaIngredients(Interface):
    def getCost(a):
        pass

    def getDescription(a):
        pass
