class User:
    # __init__ will be called everytime you create new object from this class
    # self is the actual object that's being created/initialized
    # can pass in as many parameters as you want, receive that data and use it to set the object's attribute
    def __init__(self, user_id, username):
        # creating object attributes using parameters/arguments
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method always needs self as the 1st parameter
    def follow(self, user):
        user.followers += 1     # Person you follow has their followers go up 1
        self.following += 1     # Your following goes up 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "elvin"

# This is a constructor
user_1 = User("001", "elvin")

print(user_1.id)
print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "diana"

user_2 = User("002", "diana")

# ------ ADDING METHODS TO A CLASS -----
# when a function is attached to a class it's called a method

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

