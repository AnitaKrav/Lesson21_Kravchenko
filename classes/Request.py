from exceptions import InvalidRequest, InvalidStorage


class Request:

    def __init__(self, request: str, storages: dict):

        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            raise InvalidRequest

        self.departure = parsed_request[4]
        self.destination = parsed_request[6]
        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]

        if self.departure not in storages.keys() or self.destination not in storages.keys():
            raise InvalidStorage
