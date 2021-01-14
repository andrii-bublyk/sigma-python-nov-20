class Circle:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.num = num

    def __iter__(self):
        return CircleIterator(self)


class CircleIterator:
    def __init__(self, circle: Circle):
        self.circle = circle
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.circle.num:
            raise StopIteration

        current_value = self.circle.sequence[self.current_index % len(self.circle.sequence)]
        self.current_index += 1
        return current_value



seasons = ["Winter", "Spring", "Summer", "Autumn"]
max_times = 7
circle = Circle(seasons, max_times)

for season in circle:
    print(season)
