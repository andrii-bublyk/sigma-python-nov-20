def circle_generator(sequence, num):
    """
    Return sequence items. If sequence is shorter than num, sequence items will cycle.
    :param sequence:
    :param num:
    :return: sequence items generator
    """
    current_index = 0

    while current_index < num:
        yield sequence[current_index % len(sequence)]
        current_index += 1


seasons = ["Winter", "Spring", "Summer", "Autumn"]
max_times = 7
circle = circle_generator(seasons, max_times)

for season in circle:
    print(season)
