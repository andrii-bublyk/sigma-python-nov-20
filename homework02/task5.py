cards_dict = {
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1,
    "6": 1,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": -1,
    "J": -1,
    "Q": -1,
    "K": -1,
    "A": -1
}

user_cards_string = input("enter cards: ")
clear_cards_string = user_cards_string.replace(" ", "").replace("'", "")
user_cards = clear_cards_string.split(",")

user_cards_weight = 0

for card in user_cards:
    if card in cards_dict:
        user_cards_weight += cards_dict.get(card)
    else:
        raise ValueError(f"there is no card '{card}'")

print(f"total weight = {user_cards_weight}")
