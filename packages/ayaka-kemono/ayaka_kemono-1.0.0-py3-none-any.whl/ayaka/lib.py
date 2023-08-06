import os
import requests
import urllib
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_html(url):
    r = requests.get(url)
    return r

def has_post(artist_id, p):
    r = get_html(f"https://kemono.party/fanbox/user/{artist_id}?o={str(p * 50)}")
    s = BeautifulSoup(r.content, 'html.parser')
    
    s = s.find('article', {'class': 'post-card'})
    if s:
        return True
    else:
        return False
    
def get_posts(artist_id, p):
    r = get_html(f"https://kemono.party/fanbox/user/{artist_id}?o={str(p * 50)}")
    s = BeautifulSoup(r.content, 'html.parser')
    
    cards = s.find_all('article', {'class': 'post-card'})
    
    urls = []
        
    for card in cards:
        try:
            a = card.find('a', href=True)
            urls.append(a['href'])
        except:
            pass
    
    return urls


def get_post_urls(artist_id):
    urls = []
    
    # https://kemono.party/fanbox/user/[ARTIST_ID]?o=0
    
    p = 0
    
    while has_post(artist_id, p):
        urls.extend(get_posts(artist_id, p))
        p += 1
        
    return urls

def get_images_from_post(post_url, path):
    r = get_html(f"https://kemono.party{post_url}")
    s = BeautifulSoup(r.content, 'html.parser')
    
    images = []
    
    for image in s.find_all('a', {'class': 'fileThumb'}, href=True):
        try:
            images.append(image['href'])
        except:
            pass
        
    print(post_url)
    path = os.path.join(path, post_url.split('/')[-1])
        
    try:
        os.mkdir(path)
    except:
        pass
        
    with ThreadPoolExecutor() as executor:
        for index, image in enumerate(images):
            filename = f"{index}.jpg"
            executor.submit(download, image, path, filename)
    
    
def download(url, path, filename):
    urllib.request.urlretrieve(url, os.path.join(path, filename))

def get_all_images(post_urls, path):
    for post_url in post_urls:
        get_images_from_post(post_url, path)
        

def download_from_artist(artist_id, path=''):
    # r = get_html(f"https://kemono.party/fanbox/user/{artist_id}?o=0")
    # s = BeautifulSoup(r.content, 'html.parser')
    # print(s.prettify())
    try:
        print("Discovering images...")
        post_urls = get_post_urls(artist_id)
        
        
        print("Downloading images...")
        get_all_images(post_urls, path)
    except Exception as e:
        print("Error: ", e)