# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    """
    Класс, описывающий автомобиль.

    Атрибуты:
        make (str): Производитель автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.

    Mетоды:
        start_engine() -> str:
            Запускает двигатель автомобиля.

        stop_engine() -> str:
            Останавливает двигатель автомобиля.
    """

    def __init__(self, make: str, model: str, year: int):
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("Производитель и модель должны быть строками.")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом.")
        if year < 1886 or year > 2024:
            raise ValueError("Год выпуска должен быть между 1886 и 2024.")
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """Запускает двигатель автомобиля.

        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.start_engine()
        'Двигатель запущен.'
        """
        return f"Двигатель запущен."

    def get_info(self) -> str:
        """Возвращает информацию об автомобиле в формате строки.

        Пример:
        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.get_info()
        'Toyota Camry, 2020'
        """
        return f"{self.make} {self.model}, {self.year}"

class Tree:
    """
    Класс, описывающий дерево.

    Атрибуты:
        species (str): Вид дерева.
        height (float): Высота дерева в метрах.
        age (int): Возраст дерева в годах.

    Методы:
        grow(years: int) -> str:
            Увеличивает возраст дерева на заданное количество лет.

        shed_leaves() -> str:
            Сбрасывает листья дерева.
    """

    def __init__(self, species: str, height: float, age: int):
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(height, (float, int)) or height < 0:
            raise ValueError("Высота дерева должна быть неотрицательным числом.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом.")
        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> str:
        """Увеличивает возраст дерева на заданное количество лет.
        >>> tree = Tree("Дуб", 6.0, 12)
        >>> tree.grow(5)
        'Дерево Дуб выросло.'
        """
        return f"Дерево {self.species} выросло."
    def change_season(self, season: str) -> str:
        """Изменяет состояние дерева в зависимости от сезона.
        >>> tree = Tree("Клён", 6.0, 12)
        >>> tree.change_season("осень")
        'Дерево Клён готовится к сбросу листьев.'
        """
        seasons = {
            "весна": f"Дерево {self.species} распускает новые листья.",
            "лето": f"Дерево {self.species} полное зелени.",
            "осень": f"Дерево {self.species} готовится к сбросу листьев.",
            "зима": f"Дерево {self.species} спит под снегом."
        }
        return seasons.get(season.lower(), "Неверное время года. Пожалуйста, введите 'весна', 'лето', 'осень' или 'зима'.")

class Bed:
    """
    Класс, описывающий кровать.

    Атрибуты:
        size (str): Размер кровати: "однокомнатная", "двухспальная", "королевская"
        material (str): Материал, из которого изготовлена кровать (например, "дерево", "металл").
        has_headboard (bool): Наличие изголовья (True или False).

    Методы:
        make_bed() -> str:
            Укладывает постельное белье на кровать.

        change_sheets() -> str:
            Меняет простыни на кровати.
    """

    def __init__(self, size: str, material: str, has_headboard: bool):
        if size not in ["однокомнатная", "двухспальная", "королевская"]:
            raise ValueError("Размер кровати должен быть 'однокомнатная', 'двухспальная' или 'королевская'.")

        if not isinstance(material, str) or not material:
            raise ValueError("Материал кровати должен быть непустой строкой.")

        if not isinstance(has_headboard, bool):
            raise TypeError("has_headboard должен быть булевым значением (True или False).")
        self.size = size
        self.material = material
        self.has_headboard = has_headboard

    def make_bed(self) -> str:
        """Укладывает постельное белье на кровать.

        >>> bed = Bed("двухспальная", "дерево", True)
        >>> bed.make_bed()
        'Кровать застелена.'
        """
        return f"Кровать застелена."

    def adjust_headboard(self, new_height: int) -> str:
        """Регулирует высоту изголовья кровати.

        >>> bed = Bed("двухспальная", "дерево", True)
        >>> bed.adjust_headboard(120)
        'Высота изголовья изменена на 120 см.'
        """
        if not self.has_headboard:
            return "У этой кровати нет изголовья для регулировки."

        if new_height <= 0:
            raise ValueError("Высота изголовья должна быть положительным числом.")

        self.headboard_height = new_height
        return f"Высота изголовья изменена на {new_height} см."

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
