import requests
from bs4 import BeautifulSoup


url = "https://minfin.com.ua/currency/nbu/"
features = "html.parser"
source = requests.get(url)
main_text = source.text
soup = BeautifulSoup(main_text)
table = soup.find("table", {"class" : "sc-1x32wa2-1 dYkgjk"})
tr = table.find("p", {"class" : "sc-1x32wa2-9 glerpA"})

print(table)
print(tr)





