import requests, json
from genshi.input import HTML
import smartypants
import ez_epub
session = requests.session()
# No user agent. Wattpad now blocks all user agents containing "Python".
session.headers['User-Agent'] = ''
ILLEAGAL_FILENAME_CHARACTERS = str.maketrans(r'.<>:"/\|?*^', '-----------')
API_STORYINFO = 'https://www.wattpad.com/api/v3/stories/'
API_STORYTEXT = 'https://www.wattpad.com/apiv2/storytext'
API_GETCATEGORIES = 'https://www.wattpad.com/apiv2/getcategories'
categories = session.get(API_STORYINFO).json()
#ca = {int(k): v for k, v in categories.items()}
a = categories['stories']
#for i in a:
book = ez_epub.Book()
book.title = "Tester"
book.authors = ["RhyN"]
book.sections = []
book.impl.addCover(fileobj="https://a.wattpad.com/cover/30529655-256-k93190.jpg")
book.impl.description = HTML("ini description", encoding='utf-8') # TODO: not sure if this is HTML or text
book.impl.url = "https://www.wattpad.com/story/30529655-gone-royal"
book.impl.addMeta('publisher', 'Wattpad - scraped')
book.impl.addMeta('source', "https://www.wattpad.com/95257696-gone-royal-maddie-pov")
    #print(i['url'])
chapter_html = session.get(API_STORYTEXT, params={'id': '98438767', 'output': 'json'}).json()['text']
chapter_html = smartypants.smartypants(chapter_html)
section = ez_epub.Section()
section.html = HTML(chapter_html, encoding='utf-8')
#section.title = chapter_title
book.sections.append(section)
print(book.sections)
book.make('./ergakontol')#.format(title=book.title.translate(ILLEAGAL_FILENAME_CHARACTERS)))