from lib.student import Student
from lib.student_repository import StudentRepository

"""
all returns all records from table
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    student_repository = StudentRepository(db_connection)
    assert student_repository.all() == [
                Student(1, 'Dan', 1),
                Student(2, 'John', 1),
                Student(3, 'James', 1),
                Student(4, 'Annabel', 1),
                Student(5, 'Sarah', 2),
                Student(6, 'Holly', 2),
                Student(7, 'Amber', 2),
                Student(8, 'George', 3),
                Student(9, 'Jamie', 3),
                Student(10, 'Josh', 3)
    ]
