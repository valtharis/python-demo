from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
	app.debug = True
	app.run(host = '192.168.0.151', port=5001)
