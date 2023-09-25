from review import Review

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
    
    def add_review(self, customer, rating):
        review = Review(customer, self, rating)
        self._reviews.append(review)

    @classmethod
    def total_restaurants(cls):
        return cls.all_restaurants
    
    
restaurant = Restaurant("KFC")
restaurant1 = Restaurant("Movenpick")

all_restaurants = len(Restaurant.total_restaurants())

print(restaurant.reviews())
print(all_restaurants)

