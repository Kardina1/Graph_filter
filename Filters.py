from PIL import Image
import os

def validate_path():
    """Обработка на корректный ввод пути до изображения"""
    path = input("Введите путь к файлу: ")
    while not os.path.exists(path):
        path = input("Файл не найден. Попробуйте ещё раз: ")
    return path

def validate_value(mes: str, valid_values: list[str]) -> str:
    """Валидатор"""
    value = input(mes).lower()
    while value not in valid_values:
        value = input(f"Вы ввели неверное значение. Выберите из {valid_values}\nВвод: ")
    return value

def validate_save() -> str:
    """Корректный путь для сохранения отфильтрованного изображения"""
    while True:
        file_name = input("Куда сохранять: ")
        file_parts = file_name.split(".")
        if len(file_parts) >= 2 and file_parts[-1] in ["jpg", "jpeg", "png"]:
            return file_name
        else:
            print("Некорректное имя файла. Пожалуйста, добавьте в конце формат: jpg, jpeg или png")


class Filter:
    """Базовый класс для создания фильтров"""
    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        """
        Применяет фильтр к пикселю
        :param r, g, b: цвет пикселя
        :return: новый цвет пикселя
        """
        raise NotImplementedError()

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img: исходное изображение
        :return: новое изображение
        """
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = img.getpixel((i, j))
                new_pixel = self.apply_to_pixel(r, g, b)
                img.putpixel((i, j), new_pixel)
        return img

class Red(Filter):
    """Фильтр, который повышает красный оттенок изображения"""
    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        r = min(255, r + 100)
        new_pixel = r, g, b
        return new_pixel

class Green(Filter):
    """Фильтр, который повышает зелёный оттенок изображения"""
    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        g = min(255, g + 100)
        new_pixel = r, g, b
        return new_pixel

class Blue(Filter):
    """Фильтр, который повышает синий оттенок изображения"""
    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        b = min(255, b + 100)
        new_pixel = r, g, b
        return new_pixel

class Inverse(Filter):
    """Фильтр, который инвертирует оттенок цвета"""
    def apply_to_pixel(self, r: int, g: int, b: int) -> int:
        new_pixel = (255 - r, 255 - g, 255 - b)
        return new_pixel


filters = {
    1:{
        "name": "Красный фильтр",
        "description": "Фильтр, который повышает красный оттенок изображения",
        "class": Red()
    },
    2:{
        "name": "Зеленый фильтр",
        "description": "Фильтр, который повышает зеленый оттенок изображения",
        "class": Green()
    },
    3:{
        "name": "Синий фильтр",
        "description": "Фильтр, который повышает синий оттенок изображения",
        "class": Blue()
    },
    4:{
        "name": "Инвертирующий фильтр",
        "description": "Фильтр, который инвертирует оттенок цвета",
        "class": Inverse()
    },
}