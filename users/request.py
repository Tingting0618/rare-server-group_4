import json
import sqlite3
from models import User

Users = []

def get_all_users():
    with sqlite3.connect("./rare.db") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Users u
        """)

        users = []
        dataset = db_cursor.fetchall()

    for row in dataset:
        user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                    row['bio'], row['username'], row['password'],
                    row['profile_image_url'], row['created_on'], row['active'])
        users.append(user.__dict__)
    return json.dumps(users)

def get_single_user(id):
    with sqlite3.connect("./rare.db") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_img_url,
            u.created_on,
            u.active
        FROM Users u
        WHERE u.id = ?
        """, (id, ))

        user = []
        dataset = db_cursor.fetchone()

    for row in dataset:
        user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                    row['bio'], row['username'], row['password'],
                    row['profile_image_url'], row['created_on'], row['active'])
    
    return json.dumps(user)

def get_profile_details():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.profile_img_url,
            u.created_on,
            u.active
        FROM user u
        """)

        profiles = []
        dataset = db_cursor.fetchall()

    for row in dataset:
        user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                    row['bio'], row['username'], row['profile_image_url'], 
                    row['created_on'], row['active'])

    return json.dumps(profiles)

def upload_profile_image(new_profile_image):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User
        ( profile_image_url )
        VALUES
        ( ? )
        """, (new_profile_image['profile_image_url']))

        id = db_cursor.lastrowid
        new_profile_image['id'] = id  
        # Are above two lines neccessary for a profile image, or is this
        # just for create of a whole new user?

def deactivate_user_profile(deactivate_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE User
        ( active )
        VALUES
        ( ? )
        """, (deactivate_user_profile['active']))

        id = db_cursor.lastrowid
        deactivate_user['id'] = id

    