from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return (render_template('index.html'))


@app.route('/comments')
def comments():

    try:
        f = open('comments.txt', 'r')
        all_comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close


    return render_template('comments.html', comments=all_comments)


@app.route('/comments', methods=['POST'])
def post_comment():
    form_input = request.form.get('comment')

    f = open('comments.txt', 'a')
    f.writelines(form_input + "\n")
    f.close()

    return redirect('/comments')


app.run(debug=True, port=9876)
