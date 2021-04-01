from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/')
def tmp_view():
    app.jinja_env.line_statement_prefix = '#'
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon_view():
    return send_from_directory('static', 'favicon.ico', mimetype='image/gif')


@app.route('/codes.json')
def codes_view():
    return send_from_directory('static', 'codes.json', mimetype='application/json')
