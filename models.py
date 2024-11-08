from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<JobApplication {self.name}>'
