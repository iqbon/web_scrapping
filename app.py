import bs4
import  requests

url = 'https://jadwalsholat.pkpu.or.id/?id=308'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['Shubuh'] = d.get_text()
    elif i == 2:
        sholat['Dzuhur'] = d.get_text()
    elif i == 3:
        sholat['Ashr'] = d.get_text()
    elif i == 4:
        sholat['Maghrib'] = d.get_text()
    elif i == 5:
        sholat['Isya'] = d.get_text()
    i += 1

print(sholat)
print(sholat['Maghrib'])