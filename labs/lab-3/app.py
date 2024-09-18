"""app.py: render and route to webpages"""
from db.db import *
import os

print("Current working directory:", os.getcwd())

# create a webpage based off of the html in templates/index.html
# not required: if you want to play around with some html, feel free
# to edit templates/index.html
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)