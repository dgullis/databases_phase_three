from lib.post import Post

"""
constructs with values
"""

def test_construct_with_values():
    post = Post(1, 'post_name', '2023-10-30')
    assert post.id == 1
    assert post.post_name == 'post_name'
    assert post.start_date == '2023-10-30'

"""
has string representation
"""

def test_string_representation():
    post = Post(1, 'post_name', '2023-10-30')
    assert str(post) == "Post(1, post_name, 2023-10-30)"

"""
instances with same values are equal
"""

def test_instances_with_same_values_are_equal():
    post1 = Post(1, 'post_name', '2023-10-30')
    post2 = Post(1, 'post_name', '2023-10-30')
    assert post1 == post2