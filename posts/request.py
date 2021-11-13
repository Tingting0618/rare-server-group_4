import sqlite3
import json
from models import Post

POSTS = []


def get_all_posts():

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.ROW
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM post p
        """)
        posts = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Post(row['id'], row['user_id'],
                        row['category_id'], row['title'],
                        row['title'], row['publication_date'],
                        row['image_url'], row['content'], row['approved'])
            posts.append(post.__dict__)
        return json.dumps(posts)

# def get_single_post(id):
#     with sqlite3.connect
