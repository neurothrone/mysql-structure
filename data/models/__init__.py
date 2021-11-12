from data.db import Base

# change names of the auto-generated classes
Customer = Base.classes.customers
Employees = Base.classes.employees
Offices = Base.classes.offices
OrderDetail = Base.classes.orderdetails
Order = Base.classes.orders
Payment = Base.classes.payments
ProductLine = Base.classes.productlines
Product = Base.classes.products

from data.models import customer
from data.models import order
