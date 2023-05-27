from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample student data stored as a list of dictionaries
students_data = [
    {"id": 1, "name": "Ganesh Prasad", "total_marks": 85},
    {"id": 2, "name": "Jitu M", "total_marks": 92},
    {"id": 3, "name": "Dev D", "total_marks": 78},
    # Add more student records here
]

@app.route('/api/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('pageSize', 10))

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_students = students_data[start_index:end_index]

    return jsonify(paginated_students)

@app.route('/api/students/filter', methods=['POST'])
def filter_students():
    filter_criteria = request.json.get('filterCriteria', {})

    filtered_students = []

    for student in students_data:
        if all(student.get(key) == value for key, value in filter_criteria.items()):
            filtered_students.append(student)

    return jsonify(filtered_students)

if __name__ == '__main__':
    app.run()
