from flask import Flask, render_template

app = Flask(__name__)
jobs=[
  {"ID":1,
   "Role": "Data Analyst",
   "Location" : "Hyderabad",
   'Salary': '20,000'},
  {"ID":2,
   "Role": "Data Scientist",
   "Location" : "Banglore"}
]

@app.route("/")
def hello():
  return render_template('home.html', jobs = jobs)


if (__name__ == '__main__'):
  app.run(host='0.0.0.0', debug=True)
