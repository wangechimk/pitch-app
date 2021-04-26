from flask import Flask, render_template, redirect, url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/new_comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()

    new_comment = Comment(comment=comment, user_id=user_id, pitch_id=pitch_id)

    new_comment.save_c()
    return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, )

