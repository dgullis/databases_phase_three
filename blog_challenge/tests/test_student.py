from lib.comment import Comment

"""
constructs with values
"""

def test_constructs_with_values():
    comment = Comment(1, 'name', 1)
    assert comment.id == 1
    assert comment.name == 'name'
    assert comment.post_id == 1

"""
has string representation
"""

def test_string_representation():
    comment = Comment(1, 'name', 1)
    assert str(comment) == f"Comment({1}, {'name'}, {1})"

"""
instanes with same values are equal
"""

def test_instances_same_value_are_equal():
    comment1 = Comment(1, 'name', 1)
    comment2 = Comment(1, 'name', 1)
    assert comment1 == comment2
