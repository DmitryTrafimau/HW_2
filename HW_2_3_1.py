MENU = {
    'soup': {'price': 123, 'kkal': 240},
    'tea': {'price': 20, 'kkal': 40},
    'coffee': {'price': 32, 'kkal': 33},
    'steak': {'price': 354, 'kkal': 230},
    'pasta': {'price': 145, 'kkal': 340},
    'roll': {'price': 73, 'kkal': 330},
}
DISCOUNTS = [0, 0.02, 0.05, 0.07, 0.1]
user_order = input('что будете заказывать?')
full_order = []
final_price = final_kkal = 0
if user_order in MENU:
    while user_order:
        product = MENU[user_order]
        full_order.append(user_order)
        DISCOUNTS.append(0.1)
        discount = DISCOUNTS[len(full_order) - 1]
        final_price = final_price + product['price']
        to_pay = final_price - final_price * discount
        final_kkal = final_kkal + product['kkal']
        user_order = input('что еще будете заказывать (если ничего - нажмите Enter для завершения)')
        print('ваш заказ:', *full_order)
        print('его калорийность:', final_kkal)
        print('ваша скидка:', int(DISCOUNTS[len(full_order) - 1] * 100), '%')
        print('с вас:', to_pay)
else:
    print('такого блюда нет в меню')
