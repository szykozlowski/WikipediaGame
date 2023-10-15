import requests
from bs4 import BeautifulSoup

def get_links(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('https://en.wikipedia.org/')]
    return links

def find_path(start_page, finish_page):
    queue = [(start_page, [start_page])]
    visited = set()

    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(get_links(vertex)) - visited:
            print(f"Following link: {next}")
            if next == finish_page:
                return path + [next]
            else:
                visited.add(next)
                queue.append((next, path + [next]))
    return []
