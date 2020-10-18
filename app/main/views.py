from flask import render_template, request, redirect, url_for
#from app import app
from . import main
from ..request import get_news_sources

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    news_sources = get_news_sources()
    print(news_sources)

    title = 'Home-Welcome to the best app to get information on current affairs'

    return render_template('index.html', title = title, sources = news_sources)