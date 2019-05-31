# Example 11: using Flask with Marshmallow
from flask import Flask, request, jsonify
# We import models as well as schemas
from flask_examples.models import db, Employee
from flask_examples.schemas import ma, EmployeeSchema
app = Flask(__name__)

# Configure database as in Example 10
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)
# Marshmallow has also to be initialized. Remember that ma
# has to be initialized AFTER db engine.
ma.init_app(app)

# Instantiate schemas.
employee_schema = EmployeeSchema() # This one is for single employee
employees_schema = EmployeeSchema(many=True) # And this one for lists

# Resource for adding new employee
@app.route('/employees/', methods=['POST'])
def add_employee():
    data = request.get_json()
    # Schemas can validate incoming data. The validate methods
    # returns "errors" dict. If it is empty, the object is valid.
    errors = employee_schema.validate(data)
    if errors:
        # If there were some errors, we return them with 400 Bad Request status.
        response = jsonify(errors=errors)
        response.status_code = 400
        return response
    # In case there are no errors, we make instance of the Model and save it.
    emp = employee_schema.make_instance(data)
    db.session.add(emp)
    db.session.commit()
    # Schemas also have
    return employee_schema.jsonify(emp)

@app.route('/employees/', methods=['GET'])
def get_all_employees():
    return employees_schema.jsonify(Employee.query.all())

# Resource for getting employee of given ID
@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    emp = Employee.query.filter_by(emp_id=emp_id).first_or_404()
    return employee_schema.jsonify(emp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()