import json
from app import app, db, Student, student_schema  # Make sure to replace with your actual imports

def test_add_student_route(client, app):
    # Create a test client using the Flask app
    with app.test_client() as client:
        # Prepare data for the request
        data = {
            'name': 'John Doe',
            'age': 20,
            'grade': 'A'
        }

        # Make a POST request to the /student route with the test data
        response = client.post('/student', json=data)

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200

        # Parse the JSON response
        response_data = json.loads(response.get_data(as_text=True))

        # Assert that the response contains the expected data
        assert 'name' in response_data
        assert 'age' in response_data
        assert 'grade' in response_data

        # Optionally, you can check if the data in the response matches the input data
        assert response_data['name'] == data['name']
        assert response_data['age'] == data['age']
        assert response_data['grade'] == data['grade']

        # Optionally, you can check if the data is saved in the database
        # Note: This depends on your specific implementation and database setup
        # Example: Assuming you have a SQLAlchemy model named Student
        # and a session named db.session
        db_student = db.session.query(Student).filter_by(name=data['name']).first()
        assert db_student is not None


