import os

import requests
from bs4 import BeautifulSoup

from config.settings import session


with requests.Session() as s:
    login_request = s.post("https://www.linkedin.com/uas/login-submit?loginSubmitSource=GUEST_HOME", data=session)
    print(login_request.status_code)