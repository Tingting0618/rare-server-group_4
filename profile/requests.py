import json
import sqlite3

PROFILES = []

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
        # Are lines 17 and 18 neccessary for a profile image, or is this
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