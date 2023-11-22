import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup


nltk.download('punkt')
nltk.download('stopwords')


def get_wikipedia_text(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main text content from the page
        paragraphs = soup.find_all('p')  # Assuming paragraphs are wrapped in <p> tags

        # Combine paragraphs into a single string
        text_content = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

        return text_content
    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch content from {url}")
        return None



def preprocess_text(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return filtered_words

#This uses the wikipedia search api to get a list of relevant links
def search_wikipedia(query):
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

# Example text
input_text = "Is Italy the capital of Rome?"

# Preprocess the text
result = preprocess_text(input_text)

# Display the result
print(result)

search_string = ' '.join(result)
# Example: Search for information about "Python programming language"
query_results = search_wikipedia(search_string)

# Print the JSON results
for result in query_results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Page ID: {result['pageid']}\n")
    text = get_wikipedia_text(result['url'])
    print("text", text)
    break