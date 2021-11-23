import sqlite3
from models import User

def create_user(post_data):

    new_user = User(**post_data)
  
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
            INSERT INTO Users (
            id,first_name,last_name,email,
            username,password,is_staff
            ) VALUES(?,?,?,?,?,?,?);
        """, (
            new_user.id,
            new_user.first_name,
            new_user.last_name,
            new_user.email,
            new_user.username,
            new_user.password,
            new_user.is_staff,
        ))
    
        id=db_cursor.lastrowid
        new_user.id=id 

    return new_user


def login_user(user_data):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor() 
        db_cursor.execute("""
            select *from Users u
            where
            u.username = ?
            and 
            u.password = ?;
        """, (user_data['username'], user_data['password']))

        result = db_cursor.fetchone()

        if not result:
            return None
        else:
            return User(**result)
