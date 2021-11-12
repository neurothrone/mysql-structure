from data.models import Customer
from data.models import Order
from data.repository import customer


def get_customer_by_id(_id: int) -> "Customer":
    return customer.get_customer_by_id(_id)


def get_customers_by_name_pattern(pattern: str,
                                  sensitive: bool = True,
                                  prefixed: bool = False,
                                  suffixed: bool = False) -> list["Customer"]:
    return customer.get_customers_by_name_pattern(pattern,
                                                  sensitive=sensitive,
                                                  prefixed=prefixed,
                                                  suffixed=suffixed)


def get_all_customers() -> list["Customer"]:
    return customer.get_all_customers()


def find_all_customers_that_contain_orders_by(amount: int = 10) -> list["Order"]:
    return customer.find_all_customers_that_contain_orders_by(amount)


def find_all_orders_with_total_sum_of(amount: float) -> list["Order"]:
    return customer.find_all_orders_with_total_sum_of(amount)
