from flask import Flask, render_template, request, redirect, url_for

# Use current directory for templates and static files for simplicity in this demo structure
app = Flask(__name__, template_folder='.')

# --- Public Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/donate.html')
def donate():
    return render_template('donate.html')

@app.route('/details.html')
def details():
    return render_template('details.html')

@app.route('/calculator.html')
def calculator():
    return render_template('calculator.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

# --- User Routes ---
@app.route('/user_dashboard.html')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

@app.route('/my-causes.html')
def my_causes():
    return render_template('my-causes.html')

@app.route('/my-donations.html')
def my_donations():
    return render_template('my-donations.html')

@app.route('/raise-cause.html')
def raise_cause():
    return render_template('raise-cause.html')

# --- Admin Routes ---
@app.route('/admin-dashboard.html')
def admin_dashboard():
    return render_template('admin-dashboard.html')

@app.route('/student-list.html')
def student_list():
    return render_template('student-list.html')

@app.route('/student-view.html')
def student_view():
    return render_template('student-view.html')

@app.route('/add-notice.html')
def add_notice():
    return render_template('add-notice.html')

@app.route('/add-shorts.html')
def add_shorts():
    return render_template('add-shorts.html')

@app.route('/donor-list.html')
def donor_list():
    return render_template('donor-list.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
