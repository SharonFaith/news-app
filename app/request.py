import urllib.request,json
from .models import News_Source, News_Article

#News_Source = news_source.News_Source
#News_Article = news_article.News_Article

#getting api key
api_key = None
#getting movie base url
base_url= None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url= app.config['NEWS_API_BASE_URL']

sources = 'sources'
everything = 'everything'

def process_results(sources_list):
    '''
    function that processes the news source results and transforms them to a list of objects

    Args:
        sources_list: A list of dictionaries containing news source details
    Returns:
        sources_results: A list of sources objects 
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')

        news_source_object = News_Source(id, name, description, url, category)
        sources_results.append(news_source_object)
    
    return sources_results


def process_results2(article_list):

    '''
    function that processes the news article results and transforms them to a list of objects

    Args:
       article_list: A list of dictionaries containing news article details
    Returns:
        articles_results: A list of article objects 
    '''

    articles_results = []

    for article in article_list:
        id = article.get('source.id')
        image_url = article.get('urlToImage')
        title = article.get('title')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('url')

        if image_url != None:
            news_article_object = News_Article(id, image_url, title, description, time, url)
            articles_results.append(news_article_object)
    
    return articles_results


def get_news_sources():
    '''
    Function that gets the json response to the url request
    '''
    get_sources_url = base_url.format(sources, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def get_articles(source_id):
    '''
    function that gets json response to url request
    '''

    get_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(source_id, api_key)

    


    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        articles_results = None

        if get_article_response['articles']:
            articles_results_lists = get_article_response['articles']
           
            articles_results = process_results2(articles_results_lists)
    
    return articles_results