from lib.post import Post
from lib.post_repository import PostRepository
from lib.tag import tag
"""
#all returns all records
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/tag_directory_2.sql")
    post_repository = PostRepository(db_connection)
    assert post_repository.all() == [
        Post(1, 'apprenticeship', '2023-10-30'),
        Post(2, 'main bootcamp', '2023-10-30'),
        Post(3, 'DfE,', '2023-10-30')
    ]

def test_find_post_with_tags(db_connection):
    db_connection.seed("seeds/tag_directory_2.sql")
    post_repository = PostRepository(db_connection)
    assert post_repository.find_post_with_tags(3) == Post(3, 'DfE,', '2023-10-30', [
            tag(8, 'George', 3),
            tag(9, 'Jamie', 3),
            tag(10, 'Josh', 3)
        ])



