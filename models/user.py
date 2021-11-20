from datetime import datetime

class User():

    def __init__(self, id, first_name, last_name, email, username,
                bio='', password='', profile_image_url='',
                created_on=None, active=True):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.bio = bio
        self.username = username
        self.password = password
        self.profile_image_url = profile_image_url
        self.created_on = created_on or datetime.now()
        self.active = active

# new_user = User()

# class User():
#     def __init__(self, id, first_name,last_name,email = "", username="", password = "", is_staff=0):
#         self.id = id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.username = username
#         self.password = password
#         self.is_staff = is_staff