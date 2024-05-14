import time
import requests
from bs4 import BeautifulSoup
import re
import wikipediaapi
import random
import requests
import threading
from urllib.parse import urlparse

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

wiki = wikipediaapi.Wikipedia(user_agent='my_custom_user_agent/1.0')

def getBacklinks(title):
    PARAMS = {
    "action": "query",
    "format": "json",
    "list": "backlinks",
    "bltitle": title,
    "blredirect" : True,
    "bllimit": 1000
}
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    BACKLINKS = DATA["query"]["backlinks"]
    titles = [entry['title'] for entry in BACKLINKS]

    return titles


united_states = wiki.page("United States")

united_states_links = [link.title.lower() for link in united_states.links.values()]
def backtrack(page_title, target_pages_titles, visited=None):
    if visited is None:
        visited = set()
    
    
    visited.add(page_title)
    page = wiki.page(page_title)
    backlinks = getBacklinks(page_title)

    if not page.exists() or ':' in page_title:
        return []

    if page_title.lower() in united_states_links:
        return [page_title, target_pages_titles[0]]
    for target_page_title in target_pages_titles:
        if any(target_page_title.lower() == link.lower() for link in backlinks):
            return [page_title, target_page_title]
    for target_page_title in target_pages_titles:
        for link in backlinks:
            if target_page_title.lower() in link.lower() and link not in visited:
                path = backtrack(link, target_pages_titles, visited)
                if path:
                    return [page_title] + path
    
    links =list(page.links.values())
    random.shuffle(links)
    for link in links:
        if link.title not in visited:
            path = backtrack(link.title, target_pages_titles, visited)
            if path:
                return [page_title] + path

    return []


def frontrack(start_page, target_pages, visited=None):

    if not start_page.exists() or ':' in start_page.title:
        return []
    if visited is None:
        visited = set()
    
    visited.add(start_page.title)
    for target_page in target_pages:
        if target_page.lower() in [link.title.lower() for link in start_page.links.values()]:
            return [start_page.title, target_page]
    
    for target_page in target_pages:
        if target_pages[0] in target_page.lower():
            for link in start_page.links.values():
                if target_page.lower() in link.title.lower() and link.title not in visited:
                    path = frontrack(wiki.page(link.title), target_pages, visited)
                    if path:
                        return [start_page.title] + path
    
    links = list(start_page.links.values())
    random.shuffle(links)
    
    for link in links:
        if link.title not in visited:
            path = frontrack(wiki.page(link.title), target_pages, visited)
            if path:
                return [start_page.title] + path
    
    return []

TIMEOUT = 1800  # time limit in seconds for the search

def find_path(start_page, finish_page):
    discovered = set()
    logs = []

    # breadth first search
    start_time = time.time()
    

    start_page_title = start_page
    end_page_title = finish_page
    target_pages_titles = ["United States"]

    parsed_url = urlparse(end_page_title)
    title = parsed_url.path.split("/")[-1].replace("_", " ")
    logs.append("Done!")
    path_to_targets = backtrack(title, target_pages_titles)
    final_path_thing = path_to_targets[-1]
    reversed_path = path_to_targets[::-1]  

    parsed_url = urlparse(start_page)
    title = parsed_url.path.split("/")[-1].replace("_", " ")

    start_page = wiki.page(title)

    target_pages_titles = [final_path_thing]

    target_pages = [target.lower() for target in target_pages_titles]

    path = frontrack(start_page, target_pages)

    final_path = path + reversed_path[1:]

    for i in range(len(final_path)):    
        final_path[i] = wiki.page(final_path[i]).fullurl

    elapsed_time = time.time() - start_time
    return final_path, logs, elapsed_time, len(discovered) # return with success

    raise TimeoutErrorWithLogs("Search exceeded time limit.", logs, elapsed_time, len(discovered))
class TimeoutErrorWithLogs(Exception):
    def __init__(self, message, logs, time, discovered):
        super().__init__(message)
        self.logs = logs
        self.time = time
        self.discovered = discovered