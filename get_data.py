def data():
    from bs4 import BeautifulSoup
    import requests
    # suderinam musu puslapiukaa
    url = requests.get("http://www.kasdienapmastau.lt/").text
    soup = BeautifulSoup(url, 'html.parser')
 
    text = soup.find(class_ = 'skaitinys').get_text()
    return text