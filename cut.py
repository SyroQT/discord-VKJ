from bs4 import BeautifulSoup
import requests


def data():
    # suderinam musu puslapiukaa
    url = requests.get("http://www.kasdienapmastau.lt/").text
    soup = BeautifulSoup(url, 'html.parser')

    text = soup.find(class_='skaitinys')  # .get_text()
    return text


def cut():
    text_og = data()
    # we get "Dieno evangelija"
    start = text_og.find_all('strong')
    start = start[-1].get_text()
    # whole evangelija from "Dienos evangelija" to end
    text = text_og.get_text()
    index = text.index(start)

    bible = text[index:]

    title = text_og.find('h2', class_="title").get_text()
    place = text_og.find('h2', class_="place").get_text()
    final = title + "\n" + place + '\n' + bible
    print(final)
    return final


if __name__ == "__main__":
    cut()
