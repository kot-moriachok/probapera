import time
from typing import List, Dict, Any, Optional


class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, category: str, price: float, weight: float, description: str = ""):
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Преобразование товара в словарь"""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'weight': self.weight,
            'description': self.description
        }

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - ${self.price:.2f}, {self.weight}g"

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.category}, {self.price}, {self.weight})"


class ProductCatalog:
    """Класс для управления каталогом товаров"""

    def __init__(self):
        self.products: List[Product] = []
        self.load_sample_data()

    def load_sample_data(self):
        """Загрузка примеров товаров"""
        sample_products = [
            Product("Ноутбук", "Электроника", 999.99, 1500, "Мощный ноутбук для работы"),
            Product("Смартфон", "Электроника", 699.99, 200, "Современный смартфон"),
            Product("Кофе", "Продукты", 12.99, 500, "Свежемолотый кофе"),
            Product("Книга", "Книги", 24.99, 300, "Интересная книга"),
            Product("Футболка", "Одежда", 19.99, 150, "Хлопковая футболка"),
            Product("Наушники", "Электроника", 149.99, 250, "Беспроводные наушники"),
            Product("Шоколад", "Продукты", 5.99, 100, "Молочный шоколад"),
            Product("Мышь", "Электроника", 29.99, 100, "Компьютерная мышь"),
            Product("Джинсы", "Одежда", 49.99, 400, "Синие джинсы"),
            Product("Ручка", "Канцелярия", 2.99, 20, "Шариковая ручка")
        ]
        self.products.extend(sample_products)

    def add_product(self, product: Product):
        """Добавление товара в каталог"""
        self.products.append(product)

    def remove_product(self, product_name: str):
        """Удаление товара из каталога"""
        self.products = [p for p in self.products if p.name != product_name]

    def edit_product(self, product_name: str, **kwargs):
        """Редактирование товара"""
        for product in self.products:
            if product.name == product_name:
                for key, value in kwargs.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                break

    def get_products(self) -> List[Product]:
        """Получение всех товаров"""
        return self.products

    def find_product(self, name: str) -> Optional[Product]:
        """Поиск товара по имени"""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


class ShoppingCart:
    """Класс для управления корзиной покупок"""

    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product):
        """Добавление товара в корзину"""
        self.items.append(product)

    def remove_item(self, product_name: str):
        """Удаление товара из корзины"""
        self.items = [item for item in self.items if item.name != product_name]

    def clear(self):
        """Очистка корзины"""
        self.items = []

    def get_items(self) -> List[Product]:
        """Получение всех товаров в корзине"""
        return self.items.copy()

    def total_price(self) -> float:
        """Подсчет общей стоимости"""
        return sum(item.price for item in self.items)


    def total_weight(self) -> float:
        """Подсчет общего веса"""
        return sum(item.weight for item in self.items)


    def display(self):
        """Отображение содержимого корзины"""
        if not self.items:
            print("Корзина пуста")
            return

        print("\n" + "=" * 80)
        print("СОДЕРЖИМОЕ КОРЗИНЫ:")
        print("=" * 80)
        for i, item in enumerate(self.items, 1):
            print(f"{i:2d}. {item}")
        print("=" * 80)
        print(f"Общая стоимость: ${self.total_price():.2f}")
        print(f"Общий вес: {self.total_weight()}g")
        print("=" * 80)


class SortManager:
    """Класс для управления сортировками"""

    @staticmethod
    def bubble_sort(items: List[Product], key: str, reverse: bool = False):
        """Пузырьковая сортировка (in-place)"""
        n = len(items)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                val1 = getattr(items[j], key)
                val2 = getattr(items[j + 1], key)

                # Универсальное сравнение для разных типов данных
                if reverse:
                    need_swap = val1 < val2
                else:
                    need_swap = val1 > val2

                if need_swap:
                    items[j], items[j + 1] = items[j + 1], items[j]
                    swapped = True
            if not swapped:
                break

    @staticmethod
    def insertion_sort(items: List[Product], key: str, reverse: bool = False):
        """Сортировка вставками (in-place)"""
        for i in range(1, len(items)):
            key_item = items[i]
            j = i - 1

            while j >= 0:
                current_val = getattr(items[j], key)
                key_val = getattr(key_item, key)

                if reverse:
                    condition = current_val < key_val
                else:
                    condition = current_val > key_val

                if condition:
                    items[j + 1] = items[j]
                    j -= 1
                else:
                    break

            items[j + 1] = key_item

    @staticmethod
    def quick_sort(items: List[Product], key: str, reverse: bool = False) -> List[Product]:
        """Быстрая сортировка (возвращает новый список)"""
        if len(items) <= 1:
            return items.copy()

        pivot = items[len(items) // 2]
        pivot_val = getattr(pivot, key)

        left = []
        middle = []
        right = []

        for item in items:
            item_val = getattr(item, key)

            if reverse:
                if item_val > pivot_val:
                    left.append(item)
                elif item_val < pivot_val:
                    right.append(item)
                else:
                    middle.append(item)
            else:
                if item_val < pivot_val:
                    left.append(item)
                elif item_val > pivot_val:
                    right.append(item)
                else:
                    middle.append(item)

        return (SortManager.quick_sort(left, key, reverse) +
                middle +
                SortManager.quick_sort(right, key, reverse))

    @staticmethod
    def merge_sort(items: List[Product], key: str, reverse: bool = False) -> List[Product]:
        """Сортировка слиянием (возвращает новый список)"""
        if len(items) <= 1:
            return items.copy()

        mid = len(items) // 2
        left = SortManager.merge_sort(items[:mid], key, reverse)
        right = SortManager.merge_sort(items[mid:], key, reverse)

        return SortManager._merge(left, right, key, reverse)




    @staticmethod
    def _merge(left: List[Product], right: List[Product], key: str, reverse: bool) -> List[Product]:
        """Слияние двух отсортированных списков"""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            left_val = getattr(left[i], key)
            right_val = getattr(right[j], key)

            if reverse:
                if left_val >= right_val:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            else:
                if left_val <= right_val:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


    @staticmethod
    def sort_cart(cart: ShoppingCart, algorithm: str, key: str, reverse: bool = False):
        """Сортировка корзины с выбранным алгоритмом"""
        if not cart.items:
            print("Корзина пуста, нечего сортировать!")
            return

        try:
            if algorithm == "bubble":
                # In-place сортировка
                SortManager.bubble_sort(cart.items, key, reverse)
            elif algorithm == "insertion":
                # In-place сортировка
                SortManager.insertion_sort(cart.items, key, reverse)
            elif algorithm == "quick":
                # Возвращает новый список
                cart.items = SortManager.quick_sort(cart.items, key, reverse)
            elif algorithm == "merge":
                # Возвращает новый список
                cart.items = SortManager.merge_sort(cart.items, key, reverse)
            else:
                raise ValueError(f"Неизвестный алгоритм сортировки: {algorithm}")
        except Exception as e:
            print(f"Ошибка при сортировке: {e}")


class StoreApp:
    """Основной класс приложения магазина"""

    def __init__(self):
        self.catalog = ProductCatalog()
        self.cart = ShoppingCart()
        self.sort_manager = SortManager()

    def display_catalog(self):
        """Отображение каталога товаров"""
        print("\n" + "=" * 80)
        print("КАТАЛОГ ТОВАРОВ:")
        print("=" * 80)
        products = self.catalog.get_products()
        for i, product in enumerate(products, 1):
            print(f"{i:2d}. {product}")
        print("=" * 80)

    def add_to_cart(self):
        """Добавление товара в корзину"""
        self.display_catalog()
        try:
            choice = int(input("\nВведите номер товара для добавления в корзину: ")) - 1
            products = self.catalog.get_products()
            if 0 <= choice < len(products):
                product_to_add = products[choice]
                self.cart.add_item(product_to_add)
                print(f"Товар '{product_to_add.name}' добавлен в корзину!")
            else:
                print("Неверный номер товара!")
        except ValueError:
            print("Пожалуйста, введите число!")
        except Exception as e:
            print(f"Ошибка при добавлении товара: {e}")

    def remove_from_cart(self):
        """Удаление товара из корзины"""
        if not self.cart.get_items():
            print("Корзина пуста!")
            return

        self.cart.display()
        try:
            choice = int(input("\nВведите номер товара для удаления из корзины: ")) - 1
            items = self.cart.get_items()
            if 0 <= choice < len(items):
                removed_item = items[choice]
                self.cart.remove_item(removed_item.name)
                print(f"Товар '{removed_item.name}' удален из корзины!")
            else:
                print("Неверный номер товара!")
        except ValueError:
            print("Пожалуйста, введите число!")
        except Exception as e:
            print(f"Ошибка при удалении товара: {e}")


    def sort_cart_menu(self):
        """Меню сортировки корзины"""
        if not self.cart.get_items():
            print("Корзина пуста!")
            return

        print("\n" + "=" * 80)
        print("СОРТИРОВКА КОРЗИНЫ")
        print("=" * 80)
        print("Доступные алгоритмы:")
        print("1. Пузырьковая сортировка")
        print("2. Сортировка вставками")
        print("3. Быстрая сортировка")
        print("4. Сортировка слиянием")

        print("\nКритерии сортировки:")
        print("1. По цене")
        print("2. По весу")
        print("3. По категории")

        print("\nПорядок сортировки:")
        print("1. По возрастанию")
        print("2. По убыванию")

        try:
            algo_choice = int(input("\nВыберите алгоритм сортировки (1-4): "))
            key_choice = int(input("Выберите критерий сортировки (1-3): "))
            order_choice = int(input("Выберите порядок сортировки (1-2): "))

            if not (1 <= algo_choice <= 4 and 1 <= key_choice <= 3 and 1 <= order_choice <= 2):
                print("Неверный выбор!")
                return

            algorithms = ["bubble", "insertion", "quick", "merge"]
            keys = ["price", "weight", "category"]
            reverse = order_choice == 2

            print(f"\nНачало сортировки ({algorithms[algo_choice - 1]}) по {keys[key_choice - 1]}...")
            start_time = time.time()

            # Выполняем сортировку
            self.sort_manager.sort_cart(
                self.cart,
                algorithms[algo_choice - 1],
                keys[key_choice - 1],
                reverse
            )

            end_time = time.time()
            print(f"Сортировка завершена за {end_time - start_time:.4f} секунд")

            # Показываем результат
            print("\nРезультат сортировки:")
            self.cart.display()

        except ValueError:
            print("Пожалуйста, введите числа!")
        except Exception as e:
            print(f"Ошибка при сортировке: {e}")


    def run(self):
        """Запуск основного цикла приложения"""
        while True:
            print("\n" + "=" * 80)
            print("ВИРТУАЛЬНЫЙ МАГАЗИН")
            print("=" * 80)
            print("1. Просмотреть каталог товаров")
            print("2. Добавить товар в корзину")
            print("3. Просмотреть корзину")
            print("4. Удалить товар из корзины")
            print("5. Отсортировать корзину")
            print("6. Очистить корзину")
            print("7. Выход")
            print("=" * 80)

            try:
                choice_input = input("Выберите действие (1-7): ").strip()
                if not choice_input:
                    continue

                choice = int(choice_input)

                if choice == 1:
                    self.display_catalog()
                elif choice == 2:
                    self.add_to_cart()
                elif choice == 3:
                    self.cart.display()
                elif choice == 4:
                    self.remove_from_cart()
                elif choice == 5:
                    self.sort_cart_menu()
                elif choice == 6:
                    self.cart.clear()
                    print("Корзина очищена!")
                elif choice == 7:
                    print("Спасибо за покупки! До свидания!")
                    break
                else:
                    print("Неверный выбор! Пожалуйста, выберите от 1 до 7.")
            except ValueError:
                print("Пожалуйста, введите число!")
            except KeyboardInterrupt:
                print("\n\nПрограмма завершена пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")

# Основная программа
if __name__ == "__main__":
    app = StoreApp()
    app.run()