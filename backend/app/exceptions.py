
class ResourceNotFoundError(Exception):
    pass


class UserNotFoundError(ResourceNotFoundError):
    pass


class RestaurantNotFoundError(ResourceNotFoundError):
    pass


class FoodNotFoundError(ResourceNotFoundError):
    pass


class OrderNotFoundError(ResourceNotFoundError):
    pass
