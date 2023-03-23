class BaseEror(Exception):
    message = NotImplemented


class RequestError(BaseEror):
    message = NotImplemented


class CourierError(BaseEror):
    message = NotImplemented



class NotEnoughSpace(CourierError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(CourierError):
    message = "Недостаточно товара на складе, попробуйте заказать меньше"


class UnknownProduct(CourierError):
    message = "неизвестный товар"


class DifferentProduct(CourierError):
    message = "Слишком много разных товаров"


class InvalidRequest(RequestError):
    message = "Неправильный запрос"


class InvalidStorage(RequestError):
    message = "Неверный склад"
