from bs4 import BeautifulSoup
import requests
import re

wiki_pedia_base_url = 'https://en.wikipedia.org'
baseball_base_url = 'https://www.baseball-reference.com'

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

def get_parsed(url):
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    return soup

def get_parsed_remove_comment(url):
    response = requests.get(url)
    text = response.text
    text = re.sub('<!--', '', text)
    text = re.sub('-->', '', text)
    soup = BeautifulSoup(text, 'html.parser')
    return soup

def clean_name(name):
    name = re.sub('\(.*\)$', '', name).strip()
    name = re.sub('[\+\*\#\?]$', '', name)
    name = name.strip()
    return name