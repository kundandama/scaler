from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class FarmHouse:
    def getCost(self):
        return 150

    def getDescription(self):
        return "FarmHouse"