




class Customer:
    used_ids = []

    def __init__(self,customer_id,first_name, last_name, email, delivery_address, customer_type, customer_discount=None):


        if customer_id in Customer.used_ids:
            raise Exception("customer id already exists")


        Customer.used_ids.append(customer_id)
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.customer_discount = customer_discount
        self.favorite_items = []
        self.customer_gift = None



    def add_favorite_item(self, item):
     for favorite_item in self.favorite_items:
        if favorite_item.item_name == item.item_name:
            return


     self.favorite_items.append(item)



    def remove_favorite_item(self, item_name):
     for item in self.favorite_items:
        if item.item_name == item_name:
            self.favorite_items.remove(item)
            return



    def take_gift(self, gift):
      self.customer_gift = gift



    def open_gift(self):
      if self.customer_gift is None:
        print("there is no gift to open")
      else:
        self.customer_gift.open_gift()


    def __str__(self):
      return f"{self.first_name} {self.last_name}"
