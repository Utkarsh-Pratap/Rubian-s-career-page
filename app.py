from flask import Flask, render_template,jsonify

app = Flask(__name__)


JOBS = [
    {"id": 1, "job_title": "Software Engineer", "location": "Bangalore, Karnataka", "salary": "₹12,00,000 per annum"},
    {"id": 2, "job_title": "Data Analyst", "location": "Mumbai, Maharashtra", "salary": "₹8,50,000 per annum"},
    {"id": 3, "job_title": "Backend Developer", "location": "Hyderabad, Telangana"},
    {"id": 4, "job_title": "Frontend Developer", "location": "Pune, Maharashtra", "salary": "₹9,00,000 per annum"},
    {"id": 5, "job_title": "Cloud Engineer", "location": "Chennai, Tamil Nadu", "salary": "₹11,00,000 per annum"}
]

print(app.template_folder)


@app.route('/')
def hello_world():
    return render_template('home.html' , jobs= JOBS, company_name = "Rubian's")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)




# if __name__ == "__main__":
#     app.run(debug=True)