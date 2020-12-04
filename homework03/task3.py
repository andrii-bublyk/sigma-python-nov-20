def merge(l1: list, l2: list) -> list:
    zipped = list(zip(l1, l2))
    zipped.sort(key=lambda e: e[1])
    return zipped


weekdays = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
days = [7, 6, 5, 4, 3, 2, 1]

print(merge(weekdays, days))
