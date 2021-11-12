from data.models import Customer


def custom__str__(self) -> str:
    return f"{self.customerNumber}, {self.customerName}"


Customer.__str__ = custom__str__
