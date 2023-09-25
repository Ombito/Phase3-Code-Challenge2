class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self._rating)

    def review_rating(self):
        return self._rating

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
    
    @classmethod
    def all_review(cls):
        return cls.all_reviews

review1 = Review("John", "Bao Box", 4)
review2 = Review("Becky", "Blue room", 4)
total_reviews = Review.all_review()

print(review1.review_rating())
print(review2.customer())
print(total_reviews)


