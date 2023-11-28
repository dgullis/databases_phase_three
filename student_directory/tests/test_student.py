from lib.student import Student

"""
constructs with values
"""

def test_constructs_with_values():
    student = Student(1, 'name', 1)
    assert student.id == 1
    assert student.name == 'name'
    assert student.cohort_id == 1

"""
has string representation
"""

def test_string_representation():
    student = Student(1, 'name', 1)
    assert str(student) == f"Student({1}, {'name'}, {1})"

"""
instanes with same values are equal
"""

def test_instances_same_value_are_equal():
    student1 = Student(1, 'name', 1)
    student2 = Student(1, 'name', 1)
    assert student1 == student2
