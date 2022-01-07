import requests
from config import *
from lxml import html

headers = {
    "user-agent": USER_AGENT
}

response = requests.get(URL_SEED_1, headers)

parser = html.fromstring(response.text)

languages_list = parser.xpath(
    "//div[contains(@class, 'central-featured-lang')]//strong/text()")

for language in languages_list:
    print(language)

print('='*30)

languages_list_2 = parser.find_class('central-featured-lang')
for language in languages_list_2:
    print(language.text_content())
