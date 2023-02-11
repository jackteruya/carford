import enum


class Base(enum.Enum):
    @classmethod
    def options_values(cls):
        return list(map(lambda option: option.value, cls))

    def __str__(self):
        return self.value


class ColorCar(Base):
    BLUE = 'blue'
    GRAY = 'gray'
    YELLOW = 'yellow'


class ModelCar(Base):
    CONVERTIBLE = 'convertible'
    HATCH = 'hatch'
    SEDAN = 'sedan'
