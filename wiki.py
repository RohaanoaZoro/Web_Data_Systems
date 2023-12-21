import requests
from bs4 import BeautifulSoup

def get_wikipedia_text(url, no_paras):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main text content from the page
        paragraphs = soup.find_all('p')  # Assuming paragraphs are wrapped in <p> tags
        
        if(no_paras >= 0):
            paragraphs[:no_paras]

        wiki_para_arr = []
        for paragraph in paragraphs:
            wiki_para_arr.append(paragraph.get_text())

        return wiki_para_arr
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch content from {url}")
        return None

def get_wikipedia_text2(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main text content from the page
        paragraphs = soup.find_all('p')  # Assuming paragraphs are wrapped in <p> tags

        # Combine paragraphs into a single string
        # text_content = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

        return paragraphs
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch content from {url}")
        return None


#This uses the wikipedia search api to get a list of relevant links
def search_wikipedia(entity_list, important_keywords):
    query = " ".join([word+" " for word in entity_list.keys()])
    # query = query+" ".join([word+" " for word in important_keywords])

    endpoint = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': query,
        'srlimit': 5,
        'utf8': 1  # Ensure proper handling of UTF-8 characters
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    # Extract links for each search result
    search_results = []

    for result in data['query']['search']:
        title = result['title']
        page_id = result['pageid']
        url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
        search_results.append({'title': title, 'url': url, 'pageid': page_id})

    return search_results