import requests
#get page
def get_page(url):
    print('get_page')
    try:
        return requests.get(url)
    except:
        return ""

#finding the urls in the page
def get_next_target(page):
    print('get_next_target')
    start_link = page.find('<a href =')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

#printing all the links present in the page
def get_all_links(page):
    print('get_all_links')
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links
#union of lists
def Union(lst1, lst2):
    print('Union')
    final_list = list(set(lst1) | set(lst2)) 
    return final_list

#crawler
def crawl_web(seed):
    print('crawl_web')
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            print(content)
            add_page_to_index(index,page,content)
            list(set(tocrawl).union(get_all_links(get_page(page))))
            #union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return index

#build an index
def add_to_index(index, keyword, url):
    print('add_to_index')
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] =[url]
        
#find in index
def lookup(index, keyword):
    print('lookup')
    if keyword in index:
        return index[keyword]
    else:
        return None

#building the web index
def add_page_to_index(index, url,content):
    print('add_page_to_index')
    words = content.split()
    for word in words:
        add_to_index(index,word,url)
    print(index)
    

idx = crawl_web("www.udacity.com")
print(idx)

