class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def __str__(self):
        items_str = "\n".join([f"{item}: ${price}" for item, price in self.items.items()])
        return f"Магазин: {self.name}\nАдрес: {self.address}\nАссортимент:\n{items_str if items_str else 'Пусто'}"

# Создание магазинов
store1 = Store("Магазин у дома", "ул. Ленина, 1")
store2 = Store("Супермаркет", "пр. Мира, 45")
store3 = Store("Магазин электроники", "ул. Технологическая, 22")

# Добавление товаров в магазин 1
store1.add_item("Хлеб", 1.5)
store1.add_item("Молоко", 0.9)
store1.add_item("Яблоки", 2.2)

# Добавление товаров в магазин 2
store2.add_item("Сахар", 1.1)
store2.add_item("Мука", 0.8)
store2.add_item("Кофе", 5.5)

# Добавление товаров в магазин 3
store3.add_item("Ноутбук", 500)
store3.add_item("Телефон", 300)
store3.add_item("Наушники", 50)

# Вывод информации о магазинах
print(store1)
print()
print(store2)
print()
print(store3)
