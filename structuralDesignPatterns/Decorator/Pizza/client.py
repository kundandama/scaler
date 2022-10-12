from structuralDesignPatterns.Decorator.Pizza.BasePizzas.BBQChicken import BBQChicken
from structuralDesignPatterns.Decorator.Pizza.Toppings.Cheese import Cheese
from structuralDesignPatterns.Decorator.Pizza.Toppings.Tomato import Tomato
from structuralDesignPatterns.Decorator.Pizza.Toppings.Paneer import Paneer

if __name__ == "__main__":
    my_pizza = Paneer(Cheese(Tomato(BBQChicken())))
    print(f"Pizza description :{my_pizza.getDescription()}")
    print(f" Pizza Cost : {my_pizza.getCost()}")
