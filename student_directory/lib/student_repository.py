from lib.student import Student
class StudentRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM students')
        students = [
            Student(row['id'], row['name'], row['cohort_id']) for row in rows
        ]
        return students
    

    
