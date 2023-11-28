from lib.comment import Comment
from lib.comment_repository import CommentRepository

"""
all returns all records from table
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/comment_directory_2.sql")
    comment_repository = CommentRepository(db_connection)
    assert comment_repository.all() == [
                Comment(1, 'Dan', 1),
                Comment(2, 'John', 1),
                Comment(3, 'James', 1),
                Comment(4, 'Annabel', 1),
                Comment(5, 'Sarah', 2),
                Comment(6, 'Holly', 2),
                Comment(7, 'Amber', 2),
                Comment(8, 'George', 3),
                Comment(9, 'Jamie', 3),
                Comment(10, 'Josh', 3)
    ]
