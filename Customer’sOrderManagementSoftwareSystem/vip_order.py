

from order import Order
from customer_type import CustomerType


class VipOrder(Order):

    def __init__(self, order_id, name, delivery_address, items, order_customer, payment_type, order_date):
        super().__init__(order_id, name, delivery_address, items, order_customer, payment_type, order_date)


    def calculate_total_price(self):
        if self.order_customer.customer_type != CustomerType.VIP:
            raise ValueError("Only VIP customers can make VIP orders")


        total = 0


        for item in self.items:
            total += item.item_price


        discount = self.order_customer.customer_discount

        if discount is None:
            discount = 0


        final_price = total - (total *(discount / 100))

        return final_price