from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



ma = Marshmallow(app)

db = SQLAlchemy(app)

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'grade')
        
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# create a student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(10))
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# create a database
with app.app_context():
    db.create_all()
        
# create a api add student
@app.route('/student', methods=['POST'])
def add_student():
    name = request.json['name']
    age = request.json['age']
    grade = request.json['grade']
    
    new_student = Student(name, age, grade)
    
    db.session.add(new_student)
    db.session.commit()
    
    return student_schema.jsonify(new_student)

# create a api get all students
@app.route('/students', methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

# create a api get student by id
@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)

if __name__ == '__main__':
    app.run(debug=True)