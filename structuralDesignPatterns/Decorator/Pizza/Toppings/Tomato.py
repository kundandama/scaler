from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class Tomato:
    def __init__(self, basepizza):
        self.basepizza = basepizza

    def getCost(self):
        return self.basepizza.getCost() + 30

    def getDescription(self):
        return self.basepizza.getDescription() + "+ Tomato"