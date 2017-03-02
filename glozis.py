import os
import urllib.request
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

MAIN_PAGE = 'https://www.etsy.com/ru/shop/GlozisDecor/items'
UA = UserAgent().chrome
ACCEPT_LANGUAGE = 'en=gb'
DIV_CLASS_IDENTIFYING_LINKS_TO_ITEMS = 'buyer-card'
TAG_WITH_LINK_TO_IMAGE = 'li'
IMAGE_ATTRIBUTE = 'data-full-image-href'
DESTINATION_FOLDER = 'C:\\projects\\uacrafted\\Pictures\\glozis\\'


def get_soup(url):
    header = {'user-agent': UA, 'Accept-Language': ACCEPT_LANGUAGE}
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup

soup = get_soup(MAIN_PAGE)
links_to_items = [link.get('href') for link in soup.find_all('a', class_=DIV_CLASS_IDENTIFYING_LINKS_TO_ITEMS)]
items_id = [link.get('data-listing-id') for link in soup.find_all('a', class_=DIV_CLASS_IDENTIFYING_LINKS_TO_ITEMS)]
paths = [DESTINATION_FOLDER + item_id + '\\' for item_id in items_id]

# for path in paths:
#     if not os.path.exists(path):
#         os.makedirs(path)

path_index = 0

for link_to_item in links_to_items:
    print('Fetching images for ' + paths[path_index])

    if not os.path.exists(paths[path_index]):
        os.makedirs(paths[path_index])

    soup = get_soup(link_to_item)

    links_to_images = []

    for tag_with_link_to_image in soup.find_all(TAG_WITH_LINK_TO_IMAGE):
        link_to_image = tag_with_link_to_image.get(IMAGE_ATTRIBUTE)
        if link_to_image is not None:
            links_to_images.append(link_to_image)

    for link_to_image in links_to_images:
        filename = link_to_image.split('/')[-1]
        urllib.request.urlretrieve(link_to_image, paths[path_index] + filename)

    path_index += 1

# print(links_to_images)




