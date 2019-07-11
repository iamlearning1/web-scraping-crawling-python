from bs4 import BeautifulSoup
import requests
from random import choice

data = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(data.text, 'html.parser')

contents = soup.select('.quote')

quotes = []

for content in contents:
    author_details = content.select('.author')[0]
    quote = content.select('.text')[0].get_text()
    author = author_details.get_text()
    link = author_details.find_next()['href']
    quotes.append({"quote": quote, "author": author, "link": link})

random_quote = choice(quotes)

print('Who said it ?')
print(random_quote["quote"])

count = 4

while count is not 0:
    print(f'You have {count} guesses remaining')
    guess = input()
    if guess == random_quote['author']:
        print('You won')
        break
    if count is 4:
        link = random_quote['link']
        url = 'http://quotes.toscrape.com' + link
        data = requests.get(url)
        soup = BeautifulSoup(data.text, 'html.parser')
        born_date = soup.select('.author-born-date')[0].get_text()
        born_location = soup.select('.author-born-location')[0].get_text()
        print(f'The author was born {born_location}. And dob is {born_date}')
    if count is 1:
        print('Do you want to play again (Y/N) ?')
        choice = input()
        if choice is 'Y':
            count = 5
        else:
            print(f"Author name was {random_quote['author']}")
            break
    count -= 1
