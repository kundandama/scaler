from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class BBQChicken:
    def getCost(self):
        return 200

    def getDescription(self):
        return "BBQChicken"
