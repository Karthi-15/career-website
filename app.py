from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [{
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 10,00,000'
# }, {
#     'id': 2,
#     'title': 'Data scientist',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 15,00,000'
# }, {
#     'id': 3,
#     'title': 'Front Engineer',
#     'location': 'Chennai, India',
#     'salary': 'Rs. 12,00,000'
# }, {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'Hyderabad, India',
#     'salary': 'Rs. 20,00,000'
# }]


@app.route('/')
def hello_nexatech():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='NEXATECH')


@app.route("/api/jobs")
def listjobs():
    return jsonify(jobs=load_jobs_from_db())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
