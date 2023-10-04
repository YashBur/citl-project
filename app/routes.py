#contains the API functions that the API will invoke.
import os
from . import create_app
from .models import Job
from . import db
from flask import jsonify, redirect, request, abort, render_template, url_for
import requests

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/")
def index():
    jobs = Job.query.all()
    return render_template("index.html", jobs=jobs)


@app.route("/job/list", methods = ["GET"])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_json() for job in jobs])

@app.route("/job/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job= Job.query.get(job_id)
    if job is None:
       abort(400,'Job not found')
    return render_template("job.html", job_id = job_id)

@app.route("/job/<int:job_id>", methods = ["DELETE"])
def delete_job(job_id):
    job = Job.query.get(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'result': True})

@app.route('/add_job', methods=['POST'])
def add_job():
    if not request.form:
        abort(400)
    job = Job(
        job_id=request.form.get('job_id'),
        job_Title=request.form.get('job_Title'),
        comp_name=request.form.get('comp_name'),
        Job_desc=request.form.get('Job_desc'),
        salary=request.form.get('salary')
    )
    db.session.add(job)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/create_job', methods=['POST'])
def create_job():
    if not request.json:
        abort(400)
    job = Job(
        job_id=request.json.get('job_id'),
        job_Title=request.json.get('job_Title'),
        comp_name=request.json.get('comp_name'),
        Job_desc=request.json.get('Job_desc'),
        salary=request.json.get('salary')
    )
    db.session.add(job)
    db.session.commit()
    return jsonify(job.to_json()), 201

@app.route('/job/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    job.job_Title = request.json.get('job_Title', job.job_Title)
    job.comp_name = request.json.get('comp_name', job.comp_name)
    job.Job_desc = request.json.get('Job_desc', job.Job_desc)
    job.salary = request.json.get('salary', job.salary)
    db.session.commit()
    return jsonify(job.to_json())


@app.route('/latest_jobs')
def latest_joblist():
   url1 = "https://remote-jobs-api.p.rapidapi.com/jobs"

   querystring = {"company":"shopify"}

   headers1 = {
	"X-RapidAPI-Key": "cd8ab388b9mshae264f8b24d4c13p1d991ejsn9d8db93fec8b",
	"X-RapidAPI-Host": "remote-jobs-api.p.rapidapi.com"
   }

   response1 = requests.get(url1, headers=headers1, params=querystring)

   remote_data =  response1.json()

   url = "https://linkedin-jobs-search.p.rapidapi.com/"

   payload = {
        "search_terms": "Web Developer",
        "location": "Pune, IN",
        "page": "1"
    }
   headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4110b8035fmsh91b96aa1f14068fp135075jsnbf4d5b9360fa",
        "X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
    }

   response = requests.post(url, json=payload, headers=headers)
   jobs_data = response.json()
   return render_template('index2.html', jobs_data=jobs_data, remote_data=remote_data)

@app.route("/others_job")
def home():

 return render_template("om.html")

