import wikipediaapi
import random
wiki = wikipediaapi.Wikipedia(user_agent='my_custom_user_agent/1.0')

def backtrack(page_title, target_pages_titles, visited=None):
    if visited is None:
        visited = set()
    
    
    visited.add(page_title)
    print('.')    
    page = wiki.page(page_title)
    if not page.exists() or ':' in page_title:
        return []
    for target_page_title in target_pages_titles:
        if any(target_page_title.lower() == link.title.lower() for link in page.backlinks.values()):
            return [page_title, target_page_title]
        
    for target_page_title in target_pages_titles:
        for link in page.backlinks.values() :
            if target_page_title.lower() in link.title.lower() and link.title not in visited:
                path = backtrack(link.title, target_pages_titles, visited)
                if path:
                    return [page_title] + path
        
    for link in page.links.values():
        if link.title not in visited:
            path = backtrack(link.title, target_pages_titles, visited)
            if path:
                return [page_title] + path

    
    return []


def frontrack(start_page, target_pages, visited=None):

    if visited is None:
        visited = set()
    
    visited.add(start_page.title)
    print('.')    
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





start_page_title = input("Enter a Start Page: ")
end_page_title = input("Enter an End Page: ")
target_pages_titles = ["United States", "International Standard Book Number", "Geographic coordinate system","Virtual International Authority File","Time zone","Animal","WorldCat","Japan"]

print("Backtracking...")
path_to_targets = backtrack(end_page_title, target_pages_titles)
final_path_thing = path_to_targets[-1]
reversed_path = path_to_targets[::-1]  

print(final_path_thing)
print("Frontracking...")


start_page = wiki.page(start_page_title)

target_pages_titles = [final_path_thing]

target_pages = [target.lower() for target in target_pages_titles]

path = frontrack(start_page, target_pages)


print(f"Path found from '{start_page_title}' to '{end_page_title}':")
print(" -> ".join(path[:-1]) + " -> " + " -> ".join(reversed_path))