"""assoc.py: contains association tables for many to many relationships"""
from db.db import db

# join table between professors and courses
student_course = db.Table(
  'professor_course',
  # grab the professor primary key and make it a foreign key
  db.Column('professor_id', db.Integer, db.ForeignKey('professors.professor_id')),
  # grab the course primary key and make it a foreign key
  db.Column('course_id', db.Integer, db.ForeignKey('courses.course_id'))
)