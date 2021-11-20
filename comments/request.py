import json
import sqlite3
from models import Comment

Comments = []

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.comments,
        FROM Comments c
        WHERE c.id = ?
        """, (id, ))

        comments = []
        dataset = db_cursor.fetchone()

    # for row in dataset:
        comment = Comment(dataset['id'], dataset['post_id'], dataset['author_id'], dataset['content'],)
    
    return json.dumps(comment.__dict__)

def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM comments=
        WHERE id = ?
        """, (id, ))
