from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    now = datetime.now()
    while True:
        now = now.strftime("%H:%M:%S")
        return render_template('index.html', today=today, now=now)

if __name__ == "__main__":
    app.run(debug=True)
