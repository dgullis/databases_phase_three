from lib.cohort import Cohort
from lib.cohort_repository import CohortRepository
from lib.student import Student
"""
#all returns all records
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    cohort_repository = CohortRepository(db_connection)
    assert cohort_repository.all() == [
        Cohort(1, 'apprenticeship', '2023-10-30'),
        Cohort(2, 'main bootcamp', '2023-10-30'),
        Cohort(3, 'DfE,', '2023-10-30')
    ]

def test_find_cohort_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    cohort_repository = CohortRepository(db_connection)
    assert cohort_repository.find_cohort_with_students(3) == Cohort(3, 'DfE,', '2023-10-30', [
            Student(8, 'George', 3),
            Student(9, 'Jamie', 3),
            Student(10, 'Josh', 3)
        ])



