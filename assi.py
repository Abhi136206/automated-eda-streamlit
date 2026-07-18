import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org"
response = requests.get(url)

# Check status
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Page title:", soup.title.string)
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
