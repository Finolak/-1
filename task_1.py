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
        if year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Год выпуска не может быть раньше 1886.")
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

    def stop_engine(self) -> str:
        """Останавливает двигатель автомобиля.

        >>> car = Car("Toyota", "Camry", 2020)
        >>> car.stop_engine()
        'Двигатель заглушен.'
        """
        return f"Двигатель заглушен."

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
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательной.")
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
    def shed_leaves(self) -> str:
        """Сбрасывает листья дерева.
        >>> tree = Tree("Клён", 6.0, 12)
        >>> tree.shed_leaves()
        'Дерево Клён сбросило листья.'
        """
        return f"Дерево {self.species} сбросило листья."

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
    def change_sheets(self) -> str:
        """Меняет простыни на кровати.

        >>> bed = Bed("двухспальная", "дерево", True)
        >>> bed.change_sheets()
        'Простыни на кровати двухспальная заменены.'
        """
        return f"Простыни на кровати {self.size} заменены."

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
