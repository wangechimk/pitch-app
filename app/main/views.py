from flask import Flask, render_template, redirect, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')
