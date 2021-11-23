class User():

    def __init__(self, first_name,last_name,username,email = "", password = "", is_staff=0,id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = email
        self.password = password
        self.is_staff = is_staff
