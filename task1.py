import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return filtered_words


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