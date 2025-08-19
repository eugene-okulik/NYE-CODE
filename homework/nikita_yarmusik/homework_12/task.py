class Flowers:
    def __init__(self, name, height, color, cost, life_span, in_stock=True):
        self.name = name
        self.height = height
        self.color = color
        self.cost = cost
        self.life_span = life_span
        self.in_stock = in_stock


class Roses(Flowers):
    def __init__(self, height, color, cost, life_span, in_stock, petal_shape):
        super().__init__('Розы', height, color, cost, life_span, in_stock)
        self.petal_shape = petal_shape

    def __str__(self):
        return (f'Название: {self.name}, высота стебля: {self.height}, цвет: {self.color}, '
                f'форма лепестков: {self.petal_shape}, '
                f'стоимость: {self.cost}') if self.in_stock else f'{self.name} нет!'

    def __repr__(self):
        return self.__str__()


class Daisies(Flowers):
    def __init__(self, height, color, cost, life_span, in_stock, number_of_petals):
        super().__init__('Ромашки', height, color, cost, life_span, in_stock)
        self.number_of_petals = number_of_petals

    def __str__(self):
        return (f'Название: {self.name}, высота стебля: {self.height}, '
                f'цвет: {self.color}, количество лепестков: {self.number_of_petals}, '
                f'стоимость: {self.cost}') if self.in_stock else f'{self.name} нет!'

    def __repr__(self):
        return self.__str__()


class BunchOfFlowers:
    def __init__(self):
        self.all_flowers = []

    def add_flowers(self, flower):
        self.all_flowers.append(flower)

    def total_cost(self):
        return sum(f.cost for f in self.all_flowers)

    def calculate_span_life(self):
        return sum(f.life_span for f in self.all_flowers) / len(self.all_flowers)

    def sort_flowers(self, parameter):
        if hasattr(self.all_flowers[0], parameter):
            return sorted(
                self.all_flowers, key=lambda flower: getattr(flower, parameter)
            )
        return []

    def find_flowers(self, parameter, value):
        result = []
        for f in self.all_flowers:
            if parameter == "color" and f.color == value:
                result.append(f)
            elif parameter == "height" and f.height == value:
                result.append(f)
            elif parameter == "life_span" and f.life_span == value:
                result.append(f)
            elif parameter == "cost" and f.cost == value:
                result.append(f)
        return result

    def __str__(self):
        return "\n".join(str(f) for f in self.all_flowers)


premium_roses = Roses(120, "оранжевый", 200, 2, True, "помпонная")
print(premium_roses)
cheap_daisies = Daisies(60, 'белый', 70, 3, True, 8)
print(cheap_daisies)

bunch = BunchOfFlowers()
bunch.add_flowers(premium_roses)
bunch.add_flowers(cheap_daisies)


print(bunch.total_cost())
print(bunch.calculate_span_life())


print(bunch.sort_flowers('height'))

print(bunch.find_flowers('color', 'оранжевый'))
