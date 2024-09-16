"""course.py: create a table named courses in the marist database"""
from db.db import db

class Course(db.Model):
    __tablename__ = 'courses'
    course_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    semester = db.Column(db.String(40))
    year = db.Column(db.Integer)

    # create relationship with professors table. assoc table name = professor_course
    professor = db.relationship('professors', secondary = 'professor_course', back_populates = 'courses')
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"""
            "COURSE NAME: {self.name},
             SEMESTER: {self.semester},
             YEAR: {self.year}
        """
    
    def __repr__(self):
        return self.__repr__()