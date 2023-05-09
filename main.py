from bs4 import BeautifulSoup
import requests

url = 'https://web.archive.org/web/20200427175705/https://cottageinn.com/pick-a-location/'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

tags = soup.find_all('h3')

collect_info = []
for tag in tags:
    info = tag.text
    collect_info.append(info)

print(collect_info)


def main():
    """ This is the main function."""
    pass


if __name__ == "__main__":
    main()
