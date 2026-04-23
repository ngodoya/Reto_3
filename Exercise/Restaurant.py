class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = float(price)

    def total_price(self, quantity: int = 1) -> float:
        return self.price * quantity


class Beverage(MenuItem):
    def __init__(self, name, price, mlsize: str):
        super().__init__(name, price)
        self.mlsize = mlsize


class Appetizer(MenuItem):
    def __init__(self, name, price, grportion: str):
        super().__init__(name, price)
        self.grportion = grportion


class MainCourse(MenuItem):
    def __init__(self, name, price, grportion: str):
        super().__init__(name, price)
        self.grportion = grportion


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def show_menu(self):
        print("Restaurant menu")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - ${item.price:.2f}")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem, quantity: int = 1):
        if quantity > 0:
            self.items.append((item, quantity))

    def total_order(self) -> float:
        return sum(item.total_price(quantity) for item, quantity in self.items)

    def total_with_discount(self) -> float:
        total = self.total_order()
        count = sum(q for _, q in self.items)
        if count >= 6:
            return total * 0.8
        if count >= 4:
            return total * 0.9
        return total

    def show_order(self):
        print("Current order:")
        for item, quantity in self.items:
            print(f"{item.name} x{quantity} - ${item.total_price(quantity):.2f}")
        print(f"Total (no discount): ${self.total_order():.2f}")
        print(f"Total (with discount): ${self.total_with_discount():.2f}")


menu = Menu()
menu.add_item(Beverage("Coca Cola personal", 6000, "350ml"))
menu.add_item(Beverage("Beer can", 6000, "330ml"))
menu.add_item(Beverage("Jugo natural", 9500, "250ml"))
menu.add_item(Beverage("Soda", 11500, "250ml"))
menu.add_item(Appetizer("Sopa de pasta", 5000, "400gr"))
menu.add_item(Appetizer("Caldo de costilla", 4500, "400gr"))
menu.add_item(MainCourse("Crepe de pollo", 22500, "750gr"))
menu.add_item(MainCourse("Carne a la parrilla", 19000, "750gr"))
menu.add_item(MainCourse("Porcion de pizza", 7500, "200gr"))
menu.add_item(MainCourse("Hot dog", 10000, "400gr"))

if __name__ == "__main__":
    menu.show_menu()
    order = Order()
    order.add_item(menu.items[0], 1)
    order.add_item(menu.items[6], 1)
    order.add_item(menu.items[2], 2)
    order.show_order()