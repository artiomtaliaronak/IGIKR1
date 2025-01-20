class Pizza:
    def __init__(self, name, dough, sauce, topping, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.topping = topping
        self.price = price
        
    def prepare(self):
        print(f"Preparing {self.name}. Ingredients: {self.dough} dough, {self.sauce} sauce, {self.topping} topping.")
        self.bake()
        self.cut()
        self.pack()

    def bake(self):
        print(f"Baking {self.name} pizza", end = "; ")

    def cut(self):
        print(f"Cutting {self.name} pizza", end = "; ")

    def pack(self):
        print(f"Packing {self.name} pizza\n") 

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Pepperoni", "thin", "tomato", "pepperoni", 12)

class BBQPizza(Pizza):
    def __init__(self):
        super().__init__("BBQ", "thin", "bbq", "bbq beef and chicken", 14)

class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__("Seafood", "thick", "cheese", "shrimp and anchovies", 17) 

class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def show_order(self):
        print("Order:")
        for pizza in self.pizzas:
            print(f"- {pizza.name}: {pizza.price} $")
        print(f"Total: {sum(pizza.price for pizza in self.pizzas)} $") 

class Terminal:
    def __init__(self):
        self.order = Order()

    def show_menu(self):
        print("Menu:\n 1 - Pepperoni = 12$ \n 2 - BBq = 14$ \n 3 - Seafood = 17$\n")

    def prepare_order(self):
        for pizza in self.order.pizzas:
            pizza.prepare()
        print("Order prepared and ready\n\n")

    def take_order(self):
        while True:
            choice = input("Input pizza number to order pizza or any other key to finish the order: ")
            if choice == "1":
                self.order.add_pizza(PepperoniPizza())
            elif choice == "2":
                self.order.add_pizza(BBQPizza())
            elif choice == "3":
                self.order.add_pizza(SeafoodPizza())
            else:
                self.order.show_order()
                self.prepare_order()




terminal = Terminal()
p = 1
while p != 0:
    terminal.show_menu()
    terminal.take_order()
