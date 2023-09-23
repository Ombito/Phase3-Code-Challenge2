# Restaurant Review System

The Restaurant Review System is a Python project that provides a set of classes to manage customers, restaurants, and their associated reviews. This system allows users to create and manage customer profiles, restaurants, and customer reviews of restaurants. It also provides various methods to retrieve and analyze data related to customers, restaurants, and reviews.



## Customer Class

The `Customer` class represents a customer who can leave reviews for restaurants.

### Methods:

- `Customer __init__(self, name: str, family_name: str)` - Initializes a customer with a given `name` and `family_name`.

- `Customer given_name(self)` - Returns the customer's given name.

- `Customer family_name(self)` - Returns the customer's family name.

- `Customer full_name(self)` - Returns the full name of the customer, with the given name and family name concatenated in Western style.

- `Customer all()` - Returns a list of all customer instances.

- `Customer restaurants(self)` - Returns a unique list of all restaurants that the customer has reviewed.

- `Customer num_reviews(self)` - Returns the total number of reviews that a customer has authored.

- `Customer find_by_name(cls, name: str)` - Class method: Given a string of a full name, returns the first customer whose full name matches.

- `Customer find_all_by_given_name(cls, name: str)` - Class method: Given a string of a given name, returns a list containing all customers with that given name.

- `Customer add_review(self, restaurant: Restaurant, rating: int)` - Given a restaurant object and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
  


## Restaurant Class

The `Restaurant` class represents a restaurant that can be reviewed by customers.

### Methods:

- `Restaurant __init__(self, name: str)` - Initializes a restaurant with a given `name`.

- `Restaurant name(self)` - Returns the restaurant's name.

- `Restaurant reviews(self)` - Returns a list of all reviews for that restaurant.

- `Restaurant customers(self)` - Returns a unique list of all customers who have reviewed the restaurant.

- `Restaurant average_star_rating(self)` - Returns the average star rating for the restaurant based on its reviews.
  


## Review Class

The `Review` class represents a review written by a customer for a restaurant.

### Methods:

- `Review __init__(self, customer: Customer, restaurant: Restaurant, rating: int)` - Initializes a review with a customer, restaurant, and a rating (a number).

- `Review rating(self)` - Returns the rating for the restaurant.

- `Review customer(self)` - Returns the customer object for that review.

- `Review restaurant(self)` - Returns the restaurant object for that given review.

- `Review all()` - Returns a list of all reviews.
  <br>

---

## How to Use

You can use this system to manage customers, restaurants, and their reviews. Create instances of customers, restaurants, and reviews, and then use the provided methods to interact with the data. The system allows you to add reviews, find customers, find restaurants, calculate average ratings, and more.

Here are some example usages of the Restaurant Review System:

```
# Create customers
customer1 = Customer("Alvin", "Ombito")
customer2 = Customer("Susan", "Wambui")

# Create restaurants
restaurant1 = Restaurant("Bao Box")
restaurant2 = Restaurant("Faugo Gauchi")

# Customers reviews
customer1.add_review(restaurant1, 5)
customer2.add_review(restaurant1, 4)
customer2.add_review(restaurant2, 3)

# Restaurant details
restaurant1_name = restaurant1.name()
average_rating = restaurant1.average_star_rating()
customer_list = restaurant1.customers()

# Customer details
customer1_name = customer1.full_name()
customer1_reviews = customer1.restaurants()
num_reviews = customer1.num_reviews()
```


## Contributing

If you would like to contribute to the development of this project, please follow the standard GitHub pull request process.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Conclusion

Thank you for using the Restaurant and Customer Management System! We hope it helps you manage your restaurant and customer data effectively.