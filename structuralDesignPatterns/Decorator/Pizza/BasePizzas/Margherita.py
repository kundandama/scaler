from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class Margherita:
    def getCost(self):
        return 200

    def getDescription(self):
        return "Margherita"