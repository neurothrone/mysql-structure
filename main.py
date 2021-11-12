from controller import customer


def main() -> None:
    # TODO: find a customer by id
    # target_customer_id = 128  # Blauer
    # c1 = customer.get_customer_by_id(target_customer_id)
    # print(c1)

    # TODO: find customers by specified name pattern
    # customers = customer.get_customers_by_name_pattern("signal")
    # for c in customers:
    #     print(c)

    # TODO: find customers that have more than 10 orders
    # customers = customer.find_all_customers_that_contain_orders_by(amount=10)
    # for c in customers:
    #     print(c)

    # TODO: find orders that have a total sum of AMOUNT
    orders = customer.find_all_orders_with_total_sum_of(amount=10_000)
    for order in orders:
        print(order)
        # TODO: access order.total_sum
        # TODO: access order.priceEach
        # TODO: access order.quantity


if __name__ == "__main__":
    main()
