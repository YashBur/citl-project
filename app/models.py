# contains the database schema and the ORM
from . import db
class Job(db.Model):
    __tablename__ = 'jobs' 
    job_id = db.Column(db.Integer, primary_key=True)
    job_Title = db.Column(db.String(100), nullable=False)
    comp_name = db.Column(db.String(50), nullable = False)
    Job_desc = db.Column(db.String(300), nullable=False)
    salary = db.Column(db.Integer, nullable = False)

    def to_json(self):
        return {
            'job_id': self.job_id,
            'job_Title': self.job_Title,
            'comp_name': self.comp_name,
            'Job_desc': self.Job_desc,
            'salary' : self.salary
        }