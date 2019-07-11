from bs4 import BeautifulSoup
import requests
import re

data = requests.get('https://www.pinterest.com/search/pins/?q=love&rs=typed')

soup = BeautifulSoup(data.text, 'html.parser')

contents = soup.select('body')[0]

gen = (content for content in str(contents).split(
    ' ') if '.jpg' and '550x' in content)

for i in gen:
    print(i)

with open('text.txt', 'w') as file:
    file.write(str(contents))
