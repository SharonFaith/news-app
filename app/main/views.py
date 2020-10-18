from flask import render_template, request, redirect, url_for
#from app import app
from . import main
from ..request import get_news_sources, get_articles

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

@main.route('/news-source/<source_id>')
def source_articles(source_id):
    '''
    View source page that returns the news articles from a particular source
    '''
    news_articles = get_articles(source_id)

    source_name = source_id.split('-')
    source_name_format = " ".join(source_name).title()


    if news_articles == None:
        return redirect(url_for('article_error'))
    elif news_articles == [] or source_id == 'espn' or source_id == 'bbc-sport':
        return redirect(url_for('main.article_error'))
    else:    
        return render_template('source_articles.html', id = source_id, articles = news_articles, src_name = source_name_format)

@main.route('/an_error')
def article_error():

    return render_template('article_error.html')