from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class Pepperoni:
    def getCost(self):
        return 180

    def getDescription(self):
        return "Pepperoni"