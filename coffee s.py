def menu():
    menu_dict = {
        "Еспресо": 15,
        "Американо": 30,
        "Капучино": 45,
        "Лате": 25,
        "Мокко": 47,
        "Чай": 10,
        "Круасан": 26,
	"Медовий Раф": 33
    }
    return menu_dict

def get_order(menu_dict):
    order = {}
    while True:
        product = input("Введіть назву позиції (або введіть 'кінець', щоб завершити замовлення): ").capitalize()
        if product == 'Кінець':
            break
        if product in menu_dict:
            quantity = int(input(f"Введіть кількість {product}: "))
            order[product] = quantity
        else:
            print("Цього товару немає у меню.")
            add_product = input("Хочете додати цей товар у меню? (так/ні): ").lower()
            if add_product == "так":
                price = int(input("Введіть ціну за 1 шт товару: "))
                menu_dict[product] = price
                quantity = int(input(f"Введіть кількість {product}: "))
                order[product] = quantity
            else:
                continue
        add_more = input("Бажаєте додати ще щось до вашого замовлення? (так/ні): ").lower()
        if add_more != "так":
            break
    return order

def calculate_total(order, coffee_menu):
    total = 0
    for product, quantity in order.items():
        total += coffee_menu[product] * quantity
    return total

def main():
    coffee_menu = menu()
    order = get_order(coffee_menu)
    print("Ваше замовлення:")
    for product, quantity in order.items():
        print(f"{product}: {quantity} шт.")
    total = calculate_total(order, coffee_menu)
    print(f"Вартість вашого замовлення становить: {total} грн")
    print("Дякуємо за замовлення!")

if __name__ == "__main__":
    main()
