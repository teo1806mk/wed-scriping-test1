from bs4 import BeautifulSoup
import requests
# i start the skraping
sourse = requests.get('https://www.iee.ihu.gr/en/udg_courses/')
soup = BeautifulSoup(sourse.text, 'html.parser')
kapaki=[]
semester = soup.find_all('table')[6]
for row in semester.find_all('tr'):
     for cell in row.find_all('td'):
        print(cell.text)
        kapaki.append(cell.text)
        with open("keftedaki.txt", 'a', encoding='utf8' ) as fill:
            fill.write(kapaki[-1] + "\n")