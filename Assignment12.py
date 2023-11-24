from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Dummy data for testing
students = [{"id": 1, "first_name": "John", "last_name": "Smith"}]
quizzes = [{"id": 1, "subject": "Python Basics", "questions": 5, "date": "February 5, 2015"}]
results = [{"student_id": 1, "quiz_id": 1, "score": 85}]

# Route for the root URL
@app.route('/')
def index():
    return render_template('index.html')  # Create an 'index.html' template if needed

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', students=students, quizzes=quizzes, results=results)

# Add Student route
@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Handle form submission and database update here
        new_student = {"id": len(students) + 1, "first_name": request.form['first_name'], "last_name": request.form['last_name']}
        students.append(new_student)
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

# Add Quiz route
@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if request.method == 'POST':
        # Handle form submission and database update here
        new_quiz = {"id": len(quizzes) + 1, "subject": request.form['subject'], "questions": int(request.form['questions']), "date": request.form['date']}
        quizzes.append(new_quiz)
        return redirect(url_for('dashboard'))
    return render_template('add_quiz.html')

# Student Results route
@app.route('/student/<int:id>')
def student_results(id):
    # Retrieve and display quiz results for the specified student
    student_results = [result for result in results if result['student_id'] == id]
    return render_template('student_results.html', student_id=id, results=student_results)

if __name__ == '__main__':
    app.run(debug=True)
