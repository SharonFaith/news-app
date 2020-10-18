from flask import render_template, request, redirect, url_for
#from app import app
from . import main

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')