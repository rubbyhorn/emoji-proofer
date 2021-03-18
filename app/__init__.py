from flask import Flask, render_template
app = Flask(__name__)


@app.route('/tmp')
def tmp():
    app.jinja_env.line_statement_prefix = '#'
    return render_template('tmp.html')
