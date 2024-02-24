from urllib import request
from bs4 import BeautifulSoup as bs


# скрипт для извлечения названий групп с Pitchfork.com
url = 'https://pitchfork.com/reviews/albums/?page='
list_of_url = []
for num in range(1,10):
    new_url = url
    new_url += str(num)
    list_of_url.append(new_url)

list_of_groups = []
for elem in list_of_url:
    html = request.urlopen(elem)
    soup = bs(html.read(), 'html.parser')
    list_of_names = soup.find_all('ul', 'artist-list review__title-artist')
    for name in list_of_names:
        if name.string in list_of_groups:
            continue
        else:
            list_of_groups.append(name.string)

print(list_of_groups)
