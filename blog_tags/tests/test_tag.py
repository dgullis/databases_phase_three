from lib.tag import Tag

"""
constructs with values
"""

def test_constructs_with_values():
    tag = Tag(1, 'name', 1)
    assert tag.id == 1
    assert tag.name == 'name'
    assert tag.post_id == 1

"""
has string representation
"""

def test_string_representation():
    tag = Tag(1, 'name', 1)
    assert str(tag) == f"tag({1}, {'name'}, {1})"

"""
instanes with same values are equal
"""

def test_instances_same_value_are_equal():
    tag1 = Tag(1, 'name', 1)
    tag2 = Tag(1, 'name', 1)
    assert tag1 == tag2
