from flask import Flask, render_template, send_from_directory
app = Flask(__name__)


@app.route('/tmp')
def tmp():
    app.jinja_env.line_statement_prefix = '#'
    return render_template('tmp.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/gif')

