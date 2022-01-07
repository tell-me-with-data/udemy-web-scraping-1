import requests
from bs4 import BeautifulSoup
from config import *

headers = {
  'user-agent':USER_AGENT
}

response = requests.get(URL_SEED_2, headers)
soup = BeautifulSoup(response.text)
questions = soup.find(id='questions')
list_question = questions.find_all('div', class_='question-summary')
for question in list_question:
  print(question.find('h3').text)
  print('='*17)
  print(question.find(class_='excerpt').text.replace('\n', '').replace('\r', '').strip())
  print('='*33)