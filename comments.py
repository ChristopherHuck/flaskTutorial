from flask import Blueprint, render_template, request, redirect

comments_blueprint = Blueprint('comments', __name__)


@comments_blueprint.route('/comments')
def comments():
    try:
        f = open('comments.txt', 'r')
        all_comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close

    return render_template('comments.html', comments=all_comments)


@comments_blueprint.route('/comments', methods=['POST'])
def post_comment():
    form_input = request.form.get('comment')

    f = open('comments.txt', 'a')
    f.writelines(form_input + "\n")
    f.close()

    return redirect('/comments')
