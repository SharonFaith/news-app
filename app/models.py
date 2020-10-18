class News_Source:
    '''
    To define news source objects
    '''
    
    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class News_Article:
    '''
    To define news article objects
    '''
    
    def __init__(self, source_id, image_url, title, description, time, url):
        self.id = source_id
        self.image_url = image_url
        self.title = title
        self.description = description
        self.time = time
        self.url = url