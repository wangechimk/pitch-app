from flask import Flask, render_template, redirect, url_for, abort, request
from . import main
from flask_login import login_required
from ..models import User, Pitch
from .form import PitchForm, UpdateProfile
from .. import db


@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category='Job').all()
    event = Pitch.query.filter_by(category='Events').all()
    advertisement = Pitch.query.filter_by(category='Advertisement').all()
    return render_template('index.html', job=job, event=event, pitches=pitches, advertisement=advertisement)


@main.route('/new_pitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch = Pitch(post=post, user_id=current_user._get_current_object().id, category=category)
        new_pitch.save_p()
        return redirect(url_for('main.index'))
    return render_template('create_pitch.html', form=form)


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


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<name>/updateProfile', methods=['POST', 'GET'])
def updateProfile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/update.html', form=form)
