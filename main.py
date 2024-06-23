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
        items_str = "\n".join([f"{item}: {price} руб." for item, price in self.items.items()])
        return f"Магазин: {self.name}\nАдрес: {self.address}\nАссортимент:\n{items_str if items_str else 'Пусто'}"

# Создание магазинов
store1 = Store("Магазин у дома", "ул. Ленина, 1")
store2 = Store("Супермаркет", "пр. Мира, 45")
store3 = Store("Магазин электроники", "ул. Космонавтов, 22")

# Добавление товаров в магазин 1
store1.add_item("Хлеб", 65.30)
store1.add_item("Молоко", 102.0)
store1.add_item("Яблоки", 85.0)

# Добавление товаров в магазин 2
store2.add_item("Сахар", 78.25)
store2.add_item("Мука", 81.72)
store2.add_item("Кофе", 231.40)

# Добавление товаров в магазин 3
store3.add_item("Ноутбук", 135270)
store3.add_item("Телефон", 65899)
store3.add_item("Наушники", 5229.99)

# Вывод информации о магазинах
print(store1)
print()
print(store2)
print()
print(store3)

# Операции с магазином 1
print("\nПроведение операций с магазином 'Магазин у дома':")

# Добавление нового товара
item_name = "Бананы"
price = 120.0
store1.add_item(item_name, price)
print(f"Добавлен товар '{item_name}' с ценой {price} руб.")

# Обновление цены товара
item_name = "Молоко"
price = 110.0
store1.update_price(item_name, price)
print(f"Обновлена цена товара '{item_name}' с ценой {price} руб.")

# Удаление товара
item_name = "Хлеб"
store1.remove_item(item_name)
print(f"Удален товар '{item_name}'")

# Запрос цены товара
item_name = "Яблоки"
price = store1.get_price(item_name)
print(f"Цена товара '{item_name}': {price} руб.")

# Вывод информации об ассортименте магазина после операций
print("Актуальная информация о магазине и его ассортименте:")
print(store1)
print()