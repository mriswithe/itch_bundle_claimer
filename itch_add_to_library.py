import getpass

import bs4
import requests
from loguru import logger
import sys

username = input("Itch.io login\nusername: ")
password = getpass.getpass("password: ")
creds = dict(username=username, password=password)

# Static URLs
login_page = "https://itch.io/login"
base_bundle_page = "https://itch.io/b/520/bundle-for-racial-justice-and-equality"

# Make session
session = requests.Session()
# Log in and get cookies/tokens
login_soup = bs4.BeautifulSoup(session.get(login_page).content, features="html5lib")
csrf_token = (
    login_soup.find("form", attrs={"method": "POST"})
    .find("input", attrs={"name": "csrf_token"})
    .get("value")
)
creds["csrf_token"] = csrf_token
login_req = session.post(login_page, data=creds)
login_req.raise_for_status()
if login_req.url == "https://itch.io/my-feed":
    logger.info("Logged in successfully!")
else:
    logger.info(
        "Failed to log in successfully! check username and password and try again."
    )
    sys.exit(1)

logger.info("Getting link to your claimed bundle")
base_bundle_soup = bs4.BeautifulSoup(
    session.get(base_bundle_page).content, features="html5lib"
)
link = base_bundle_soup.find("a", attrs={"class": "button outline forward_link"})
bundle_page = f'https://itch.io{link.get("href")}'
logger.info("Found bundle page link")
logger.info("Paging through the bundle page")

run = True
page = 1
form_dict = {"csrf_token": csrf_token, "action": "claim"}
while run:
    logger.info(f"Getting page {page}")
    soup = bs4.BeautifulSoup(
        session.get(bundle_page, params={"page": page}).content, features="html5lib"
    )
    for row in soup.find_all("div", attrs={"class": "game_row"}):
        game_name = row.find("h2", attrs={"class": "game_title"}).text
        game_id_elem = row.find("input", attrs={"name": "game_id"})
        if game_id_elem:
            logger.info(f"Claiming game {game_name}")
            game_id = game_id_elem.get("value")
        else:
            logger.info(f"Already claimed {game_name}")
            continue
        form_dict["game_id"] = game_id
        claim_resp = session.post(bundle_page, params={"page": page}, data=form_dict)
        claim_resp.raise_for_status()
    if soup.find("a", attrs={"class": "next_page button"}):
        page += 1
    else:
        run = False
logger.info("Finished!")
sys.exit(0)
