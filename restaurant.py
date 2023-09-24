class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name   

    def reviews(self):
        return self._reviews
    
    def add_review(self, review):
        self._reviews.append(review)

    @classmethod
    def total_restaurants(cls):
        return cls.all_restaurants
    
    def customers(self):      
        customers = set()

        for review in self._reviews:
            customers.add(review.customer())
        return list(customers)
    
    
restaurant = Restaurant("KFC")
restaurant1 = Restaurant("Movenpick")
all_restaurants = len(Restaurant.total_restaurants())

print(restaurant1.customers())
print(all_restaurants)

