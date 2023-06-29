from flask import Flask, render_template,jsonify

jobs = [
  {
    'id': 1,
    'title': 'Data Analyst', 
    'location': 'Toronto, Canada',
    'salary (USD)': 70000 
  },

  {
    'id': 2,
    'title': 'Data Engineer', 
    'location': 'Montreal, Canada',
    'salary (USD)': 80000 
  },

  {
    'id': 3,
    'title': 'Project Manager', 
    'location': 'Delaware, USA',
    'salary (USD)': 150000 
  }
  
]

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('home.html',
                        jobs =jobs
                        )

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)