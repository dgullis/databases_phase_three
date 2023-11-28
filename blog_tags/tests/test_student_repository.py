from lib.tag import tag
from lib.tag_repository import tagRepository

"""
all returns all records from table
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/tag_directory_2.sql")
    tag_repository = tagRepository(db_connection)
    assert tag_repository.all() == [
                tag(1, 'Dan', 1),
                tag(2, 'John', 1),
                tag(3, 'James', 1),
                tag(4, 'Annabel', 1),
                tag(5, 'Sarah', 2),
                tag(6, 'Holly', 2),
                tag(7, 'Amber', 2),
                tag(8, 'George', 3),
                tag(9, 'Jamie', 3),
                tag(10, 'Josh', 3)
    ]
