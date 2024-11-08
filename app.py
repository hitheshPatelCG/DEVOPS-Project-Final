from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, JobApplication
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

# Initialize the database if it doesn't exist
with app.app_context():
    db.create_all()

# Home - List all job applications
@app.route('/')
def index():
    applications = JobApplication.query.all()
    return render_template('index.html', applications=applications)

# Create a new job application
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        experience = request.form['experience']

        new_application = JobApplication(name=name, position=position, experience=experience)
        db.session.add(new_application)
        db.session.commit()
        flash('Application created successfully!')
        return redirect(url_for('index'))
    return render_template('create.html')

# Update an existing job application
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    application = JobApplication.query.get_or_404(id)
    if request.method == 'POST':
        application.name = request.form['name']
        application.position = request.form['position']
        application.experience = request.form['experience']
        db.session.commit()
        flash('Application updated successfully!')
        return redirect(url_for('index'))
    return render_template('update.html', application=application)

# Delete a job application
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    application = JobApplication.query.get_or_404(id)
    db.session.delete(application)
    db.session.commit()
    flash('Application deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

