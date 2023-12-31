from review import Review

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)


    @classmethod
    def total_customers(cls):
        return cls.all_customers

name = Customer("Alvin", "Ombito")
name1 = Customer("John", "Karanja")
name2 = Customer("Shiro", "Vee")


total_customers = len(Customer.total_customers())
print(total_customers)




