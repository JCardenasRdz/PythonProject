

list_of_urls = ['http://www.google.fr/', 'http://www.google.fr/', 
                'http://www.google.cn/', 'http://www.google.com/', 
                'http://www.google.fr/', 'http://www.google.fr/', 
                'http://www.google.fr/', 'http://www.google.com/', 
                'http://www.google.fr/', 'http://www.google.com/', 
                'http://www.google.cn/']

urls = [{'url': 'http://www.google.fr/', 'nbr': 1}]



urls_d = {}
for url in list_of_urls:
    if not url in urls_d:
        urls_d[url] = 1
    else:
        urls_d[url] += 1