from data.models import Order


def custom__str__(self) -> str:
    return f"{self.orderNumber}, {self.orderDate}"


Order.__str__ = custom__str__
