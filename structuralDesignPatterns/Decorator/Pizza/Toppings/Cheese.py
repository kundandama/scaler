from structuralDesignPatterns.Decorator.Pizza.IPizzaIngridients import IPizzaIngredients
from zope.interface import implementer


@implementer(IPizzaIngredients)
class Cheese:
    def __init__(self, basepizza):
        self.basepizza = basepizza

    def getCost(self):
        return self.basepizza.getCost() + 80

    def getDescription(self):
        return self.basepizza.getDescription() + "+ Cheese"