# Models for example 10 and 11
from flask_sqlalchemy import SQLAlchemy

# The db object defined below will serve as a DeclarativeBase and
# db engine.
db = SQLAlchemy()

# Models are defined as usual with SQLAlchemy, but with all objects (Columns, Table etc.)
# from db rather than raw SQLAlchemy
emp_proj = db.Table('emp_proj', db.metadata,
                 db.Column('emp_id', db.ForeignKey('employees.emp_id'), primary_key=True),
                 db.Column('proj_id', db.ForeignKey('projects.proj_id'), primary_key=True))

class Employee(db.Model):
    __tablename__ = 'employees'

    emp_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.dept_id'))

    department = db.relationship('Department', back_populates='employees')
    projects = db.relationship('Project', secondary=emp_proj, back_populates='employees')

    def __repr__(self):
        return f'{self.first_name} {self.last_name} <id {self.emp_id}>'

class Project(db.Model):

    __tablename__ = 'projects'
    proj_id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    name = db.Column(db.String)

    employees = db.relationship('Employee', secondary=emp_proj, back_populates='projects')

class Department(db.Model):
    __tablename__ = 'departments'

    dept_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, autoincrement=True)

    employees = db.relationship('Employee', back_populates='department', order_by=Employee.emp_id)

    # This converts department to a dict suitable for json representation.
    def to_dict(self):
        return {'dept_id': self.dept_id, 'name': self.name}