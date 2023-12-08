from flask import Flask
from datetime import datetime
import random

current_time = datetime.now()

app = Flask(__name__)

@app.route("/")
def index():
    result = random.randint(1, 6)
    return {"rolled": result}

@app.route("/lol")
def lol():
    global current_time
    past_time = datetime.now() - current_time
    current_time = datetime.now()
    return f"The last time was {str(past_time)}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
