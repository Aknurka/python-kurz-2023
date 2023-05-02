def validate_phone_number(number):
    if len(number) == 9:
        if number.isdigit():
            return True
    elif len(number) == 13:
        if number[0:4] == "+420" and number[4:].isdigit():
            return True
    return False

'''def calculate_price(characters):
    if len(characters) >= 180:
        return (len(characters) // 180 + 1) * 3
    else:
        return (len(characters) // 180 + 1) * 0'''

def calculate_message_price(message):
    message_length = len(message)
    if message_length < 180:
        price = 0
    elif message_length % 180 == 0:
        price = (message_length // 180) * 3
    else:
        price = (message_length // 180 + 1) * 3
    return price

phone_number = input("Zadej telefonní číslo: ")
if validate_phone_number(phone_number):
    message = input("Zadej zprávu: ")
    price = calculate_message_price(message)
    print(f"Cena zprávy je {price} Kč.")
else:
    print("Neplatné telefonní číslo.")