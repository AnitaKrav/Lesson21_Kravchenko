from classes.Request import Request
from classes.Shop import Shop
from classes.Store import Store
from exceptions import RequestError, CourierError

store = Store({
    "конфеты": 10,
    "печенье": 20,
    "яблоки": 3,
    "леденцы": 10
})

shop = Shop({
    "конфеты": 11,
    "варенье": 2,
    "груши": 3,
    "мороженое": 1
})

storages = {
    "магазин": shop,
    "склад": store
}
while True:
    print("\nДобрый день!\n")

    for storage in storages:
        print(f"Сейчас в {storage}е: \n{storages[storage].get_items()}\n")

    user_input = input(
        "Введите запрос в формате: Доставить 3 печенье из склад в магазин\n"
        "Введите Stop, если хотите завершить.:\n"
    )

    if user_input.lower() == "stop":
        break

    try:
        request = Request(request=user_input, storages=storages)
    except RequestError as error:
        print(error.message)
        continue

    try:
        storages[request.departure].remove(request.product, request.amount)
        print(f'Курьер забрал {request.amount} {request.product} из {request.departure}.')
    except CourierError as error:
        print(error.message)
        continue
    try:
        storages[request.destination].add(request.product, request.amount)
        print(f'Курьер доставил {request.amount} {request.product} в {request.destination}.')
    except CourierError as error:
        print(error.message)
        storages[request.departure].add(request.product, request.amount)
        print(f'Курьер вернул {request.amount} {request.product} в {request.departure}.')
        continue

