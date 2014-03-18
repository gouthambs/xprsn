
from flask import render_template
from xprsn import app
import jinja2


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.config.from_object('config')
    app.run(debug=True)