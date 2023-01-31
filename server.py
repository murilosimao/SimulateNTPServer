from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/now")
def current_timestamp():
    current = (datetime.utcnow() - datetime(1900, 1, 1)).total_seconds()
    current = int(current)
    current = str(current)
    return current


if __name__=="__main__":
    app.run(host="0.0.0.0")