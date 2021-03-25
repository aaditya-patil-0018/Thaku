from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    while True:
        return render_template('index.html', today=today, now=now)

if __name__ == "__main__":
    app.run(debug=True)
