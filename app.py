from flask import Flask, render_template, request
from datetime import datetime
import time
import csv

app = Flask(__name__)

data = []
db = None
@app.route('/')
def index():
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    for d in data:
        if d[1] != today:
            data.remove(d)
    return render_template('index.html', today=today, now=now, data=data, db=db)

@app.route('/', methods=["POST"])
def info():
    name = request.form.get("name")
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    li = [name, today, now]
    data.append(li)
    return index()



if __name__ == "__main__":
    app.run(debug=True)
