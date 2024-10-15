import os
from flask import Flask, render_template, jsonify
from components import JOBS

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))