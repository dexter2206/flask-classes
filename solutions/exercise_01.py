# Example 10: using Flask with SQLAlchemy
from flask import Flask, request
# The jsonify function is enhanced version of json.dumps.
# Amongst other differences, it sorts the keys, preventing disrupting of caches.
from flask.json import jsonify
# Import relevant model and engine.
from flask_examples.models import db, Department, Employee

app = Flask(__name__)

# For the engine to work we need to configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
# And initialize it with an app
db.init_app(app)

# Resource for posting departments.
@app.route('/departments', methods=['POST'])
def add_department():
    # Get data
    data = request.get_json()
    # We don't implement sophisticated validation (we will do so with Marshmallow later).
    # Here we only catch an exception (raised when name is not present) and return
    # 400 Bad Request in an exception is catched.
    try:
        dept = Department(name=data['name'])
        db.session.add(dept)
        db.session.commit()
        # Remember that jsonify can't process Model instances. That's why we convert
        # it to dict.
        return jsonify(dept.to_dict())
    except KeyError:
        # Even in case of error we return JSON encoded response.
        response = jsonify({'error': 'Bad request', 'missing field': 'name'})
        response.status_code = 400
        return response

# Resource for getting given department.
@app.route('/departments/<int:dept_id>', methods=['GET'])
def get_department(dept_id):
    # Query is done as usual with SQLAlchemy.
    # The only difference is that query sets now have (...)_or_404 methods
    # that terminate execution if query is empty.
    dept = Department.query.filter_by(dept_id=dept_id).first_or_404()
    return jsonify(dept.to_dict())

# Resource for patching department, i.e. modifying part of the object.
@app.route('/departments/<int:dept_id>', methods=['PATCH'])
def patch_department(dept_id):
    dept = Department.query.filter_by(dept_id=dept_id).first_or_404()
    # Note: usually when patching, full object is not required.
    # Therefore even an empty request is technically correct.
    # We cannot assume that 'name' is in the requests's data
    # nor throw an error in this case.
    dept.name = request.get_json().get('name', dept.name)
    db.session.add(dept)
    db.session.commit()
    return jsonify(dept.to_dict())

# Resource for deleting department
@app.route('/departments/<int:dept_id>', methods=['DELETE'])
def delete_department(dept_id):
    dept = Department.query.filter_by(dept_id=dept_id).first_or_404()
    # Database engine provides us with a session. We don't have to close it,
    # it is done automatically.
    db.session.delete(dept)
    db.session.commit()
    return ''

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()

    try:
        emp = Employee(
            first_name=data['first_name'],
            last_name=data['last_name'],
            dept_id=data.get('dept_id'))
        db.session.add(emp)
        db.session.commit()
        return jsonify(emp.to_dict())
    except KeyError:
        response = jsonify({'error': 'Bad request'})
        response.status_code = 400
        return response

@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    emp = Employee.query.filter_by(emp_id=emp_id).first_or_404()
    return jsonify(emp.to_dict())

@app.route('/employees/<int:emp_id>', methods=['PATCH'])
def patch_employee(emp_id):
    emp = Employee.query.filter_by(emp_id=emp_id).first_or_404()
    emp.first_name = request.get_json().get('first_name', emp.first_name)
    emp.last_name = request.get_json().get('last_name', emp.last_name)
    db.session.add(emp)
    db.session.commit()
    return jsonify(emp.to_dict())

# An error handler for 404 not found
# We implement it because by default HTML page with error is returned -
# we want JSON response instead.
@app.errorhandler(404)
def handle_404(error):
    return jsonify(error=404, text=str(error))

# Create database. Note that db can be used only in:
# - views (as above)
# - bocks in app context (as below)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
