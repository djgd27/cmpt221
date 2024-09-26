"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)
    FirstName = db.Column(db.String(40))
    LastName = db.Column(db.String(40))
    EmailAddress = db.Column(db.String(40))

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self, FirstName):
        # remove pass and then initialize attributes
        self.FirstName = self.FirstName
        self.LastName = self.LastName
        self.EmailAddress = self.EmailAddress

    def __repr__(self):
        # add text to the f-string
        return f"""
            "FIRST NAME: {self.FirstName}
             LAST NAME: {self.LastName},
             EMAIL ADDRESS: {self.EmailAddress}
        """
    
    def __repr__(self):
        return self.__repr__()