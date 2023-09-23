class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def first_name(self):
        return self.given_name
    
    def last_name(self):
        return self.family_name
    
    def full_name(self):
        return (f"{self.given_name} {self.family_name}")
    
    @classmethod
    def total_customers(cls):
        return cls.all_customers

name = Customer("Alvin", "Ombito")
name1 = Customer("Jan", "Kimutai")
name2 = Customer("Dan", "Kimutai")
print(name.full_name())