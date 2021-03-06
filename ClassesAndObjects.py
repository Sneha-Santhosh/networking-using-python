class RetailItem:

    # class attribute
    _id = 1

    # instance attributes
    def __init__(self, description, units, price):
        self.description = description
        self.units = units
        self.price = price
        self._id = RetailItem._id
        RetailItem._id += 1
    
    def __str__(self):
        return f'Item #{self._id} : - \n Description: {self.description} \n Units in inventory: {self.units} \n Price: ${self.price:,.2f}\n'

# objects of RetailItem class
item1 = RetailItem("Jacket", 12, 57.75)
item2 = RetailItem("Jeans", 10, 35.45)
item3 = RetailItem("Shirt", 20, 24.90)

print(item1)
print(item2)
print(item3)
name = "Jane Doe"
def myFunction(parameter):
    value = "First"
    value = parameter
    print (value)

myFunction("Second")