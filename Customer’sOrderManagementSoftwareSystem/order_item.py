


class OrderItem:
    used_ids = []


    def __init__(self, item_id, item_name , item_price):
        if item_id in OrderItem.used_ids:
            raise ValueError("Item id already exists")

        OrderItem.used_ids.append(item_id)

        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price


    def __str__(self):
      return f"{self.item_name} - {self.item_price}"
