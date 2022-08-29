#! python3

import os
import urllib.request as urllib2
import urllib.request, urllib.error, urllib.parse
from bs4 import *
from urllib.parse import urljoin
from markdownify import markdownify

def crawl(pages, depth=None):
    indexed_url = [] # a list for the main and sub-HTML websites in the main website
    for i in range(depth):
        for page in pages:
            if page not in indexed_url:
                indexed_url.append(page)
                try:
                    c = urllib2.urlopen(page)
                except:
                    print( "Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read(), features="html.parser")
                links = soup('a') #finding all the sub_links
                for link in links:
                    if 'href' in dict(link.attrs):
                        url = urljoin(page, link['href'])
                        if url.find("'") != -1:
                                continue
                        url = url.split('#')[0] 
                        if url[0:4] == 'http':
                                indexed_url.append(url)
        pages = indexed_url
    return indexed_url

def get_web_content(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), features="html.parser")
    web_content = soup.get_text()
    # print(web_content[0:300])
    return web_content

def get_title(web_content):
    soup = BeautifulSoup(web_content, features="html.parser")
    title = soup.find('title')
    print(title)
    return title

def filename_from_url(url):
    replace = ':/.'
    for r in replace:
        url = url.replace(r,'_')
    return url   


def to_md(web_content):
    md = markdownify(web_content, heading="ATX")
    return md

def write_file(filename, content):
    outputFile = open(filename, 'w')
    outputFile.write(content)
    outputFile.close()

# Pages to crawl
pagelist=["https://github.com/strategdk/tmux/blob/main/README.md"] 

# Directory of current Python script and output directory
prog_dir = os.path.dirname(os.path.abspath(__file__))
out_dir = prog_dir + '/out/' 

print(pagelist)
urls = crawl(pagelist, depth=1)

for url in urls:
  print(url)
  filename = filename_from_url(url)
  print(filename)
  web_content = get_web_content(url)
  #  title = get_title(web_content)
  md = to_md(web_content)      
  write_file(out_dir + filename + ".md", md)
