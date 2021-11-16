USERS = [
    # {
    #     "id": 1,
    #     "name": "Snickers",
    #     "species": "Dog",
    #     "locationId": 1,
    #     "customerId": 4
    # },
    {'id': 1, 
    'first_name': 'Snickers', 
    'last_name': 'Dog', 
    'email': '123@me.com', 
    'username': '123', 
    'password': '123', 
    'is_staff': 1
    },
    {'id': 2, 
    'first_name': 'Lenny', 
    'last_name': 'Cat', 
    'email': '123@me.com', 
    'username': '123', 
    'password': '123', 
    'is_staff': 0
    }
]


def get_all_users():
    return USERS

# Function with a single parameter
def get_single_user(id):
    # Variable to hold the found user, if it exists
    requested_user = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for user in USERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if user["id"] == id:
            requested_user = user

    return requested_user
