



class Order:
    used_ids = []

    def __init__(self, order_id, name, delivery_address, items, order_customer, payment_type,  order_date):


        if order_id in Order.used_ids:
            raise Exception("Order id already exists")


        Order.used_ids.append(order_id)


        self.order_id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.order_customer = order_customer
        self.payment_type = payment_type
        self.order_date = order_date


        self.add_items_to_customer_favorites()
        self.order_total_price = self.calculate_total_price()


    def calculate_total_price(self):
        total = 0

        for item in self.items:
            total += item.item_price

        return total

    def add_items_to_customer_favorites(self):
        for item in self.items:
            self.order_customer.add_favorite_item(item)


    def __str__(self):
        return f"Order {self.order_id} {self.name}, total: {self.order_total_price}"



