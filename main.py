from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return (render_template('index.html'))


@app.route('/comments')
def comments():
    return render_template('comments.html', comments=['Erster Kommentar', 'Test', 'test2'])
app.run(debug=True, port=9876)
