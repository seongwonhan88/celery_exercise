import requests
from bs4 import BeautifulSoup

from config.settings import session

with requests.Session() as s:
    login_request = s.post("https://www.linkedin.com/uas/login-submit?loginSubmitSource=GUEST_HOME", data=session)
    print(login_request.status_code)

    if login_request.status_code != 200:
        raise Exception('login failed!')
    feed = s.get('https://www.linkedin.com/feed/')
    soup = BeautifulSoup(feed.text, 'html.parser')
    title = soup.select('#ember71 > h3 > span > span')
    contents = soup.select('#ember101 > span')

    print(title)
