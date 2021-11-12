from data.db import session
from data.models import Customer
from data.models import Order


def get_customer_by_id(_id: int) -> "Customer":
    return session.query(Customer).filter(
        Customer.customerNumber == _id).first()


def get_customers_by_name_pattern(pattern: str,
                                  sensitive: bool = True,
                                  prefixed: bool = False,
                                  suffixed: bool = False) -> list["Customer"]:
    """...

    By default checks if the name contains the pattern when
    prefixed or suffixed is not set to True.

    """

    # use String Template
    if prefixed:
        search = f"%{pattern}"
    elif suffixed:
        search = f"{pattern}%"
    else:
        search = f"%{pattern}%"

    if sensitive:
        return session.query(Customer).filter(
            Customer.customerName.like(search)).all()

    return session.query(Customer).filter(
        Customer.customerName.ilike(search)).all()


def get_all_customers() -> list["Customer"]:
    return session.query(Customer).all()


def find_all_customers_that_contain_orders_by(amount: int = 10) -> list["Order"]:
    customers = get_all_customers()

    customers_results = []

    for customer in customers:
        if len(customer.orders_collection) >= amount:
            customers_results.append(customer)

    return customers_results


def find_all_orders_with_total_sum_of(amount: float) -> list["Order"]:
    customers = get_all_customers()

    orders_results = []

    for customer in customers:
        for order in customer.orders_collection:
            for order_row in order.orderdetails_collection:
                if order_row.priceEach * order_row.quantityOrdered >= amount:
                    orders_results.append(order)

    return orders_results
