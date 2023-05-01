def validate_phone_number(number):
    if len(number) == 9:
        if number.isdigit():
            return True
    elif len(number) == 13:
        if number[0:4] == "+420" and number[4:].isdigit():
            return True
    return False

def calculate_message_price(message):
    price_per_char = 0.01667 # 3 Kč / 180 znaků
    message_length = len(message)
    price = (message_length // 180 + 1) * 3 # cena za započaté 180 znaků
    return price

phone_number = input("Zadej telefonní číslo: ")
if validate_phone_number(phone_number):
    message = input("Zadej zprávu: ")
    price = calculate_message_price(message)
    print(f"Cena zprávy je {price} Kč.")
else:
    print("Neplatné telefonní číslo.")