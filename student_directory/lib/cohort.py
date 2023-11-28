class Cohort:
    def __init__(self, id, cohort_name, start_date, students=[]):
        self.id = id
        self.cohort_name = cohort_name
        self.start_date = start_date
        self.students = students
    
    def __repr__(self):
        return f"Cohort({self.id}, {self.cohort_name}, {self.start_date}, {self.students})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
