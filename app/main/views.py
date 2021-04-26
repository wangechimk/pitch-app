from flask import Flask, render_template, redirect, url_for
from . import main
from flask_login import login_required


@main.route('/')
def index():
    pitches = pitch.query.all()
    job = Pitch.query.filter_by(category='Job').all()
    event = Pitch.query.filter_by(category='Events').all()
    advertisement = Pitch.query.filter_by(category='Advertisement').all()
    return render_template('index.html', job=job, event=event, pitches=pitches, advertisement=advertisement)


@main.route('/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
    new_comment = Comment(comment=comment, user_id=user_id, pitch_id=pitch_id)

    new_comment.save_c()
    return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, )
