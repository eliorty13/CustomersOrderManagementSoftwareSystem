

from customer_type import CustomerType
from payment_type import PaymentType
from order_item import OrderItem
from customer import Customer
from regular_order import RegularOrder
from vip_order import VipOrder
from gift import Gift




item1 = OrderItem(1, " Keyboard",100)
item2 = OrderItem(2, " Mouse",50)
item3 = OrderItem(3, " Keyboard",150)

regular_customer = Customer(1,"Elior", "Ben Naftali", "eliorty13@gmail.com", "beer yaakov",CustomerType.REGULAR)
vip_customer = Customer(2,"dana", "cohen", "dana@gmail.com","Tel Aviv", CustomerType.VIP,20)

regular_order = RegularOrder(
    1,"Regular computer order",regular_customer.delivery_address,[item1, item2], regular_customer,PaymentType.CREDIT_CARD,"06-07-2026")

VIP_order = VipOrder(
    2, "VIP computer order", vip_customer.delivery_address,[item1, item2 ],vip_customer,PaymentType.CASH,"06-07-2026")

print(regular_order)
print(VIP_order)


print("Regular customer favorite items:")
for item in regular_customer.favorite_items:
    print(item)

print("VIP customer favorite items:")
for item in vip_customer.favorite_items:
    print(item)


gift = Gift()
vip_customer.take_gift(gift)
vip_customer.open_gift()