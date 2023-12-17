import spacy
import requests

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm") # python3 -m spacy download en_core_web_sm
text = "Deforestation in Brazil’s Amazon rainforest reached a record high for the first six months of the year, as an area five times the size of New York City was destroyed, preliminary government data showed on Friday."
doc = nlp(text)

# Extract and print named entities with their labels
for ent in doc.ents:
    print(ent.text, ent.label_)

# 1. External KB disambiguation 
def query_wikipedia(entity):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={entity}&format=json"
    response = requests.get(search_url)
    results = response.json()['query']['search']
    # Implement logic to analyze results and determine the most likely entity
    return results[0]['snippet'] if results else "Unknown"

# for ent in doc.ents:
#     disambiguated_entity = query_wikipedia(ent.text)
#     print(f"Original: {ent.text}, Disambiguated: {disambiguated_entity}")

# 2. Custom rule disambiguation
# entity_mapping = {
#     "ORG": ["Apple Inc.", "Microsoft", "Google"],
#     "PRODUCT": ["apple"],
#     "PERSON": ["Steve Jobs", "Tim Cook"]
# }

# for ent in doc.ents:
#     if ent.label_ in entity_mapping:
#         candidates = entity_mapping[ent.label_]
#         # You can use a disambiguation strategy here to select the correct entity
#         disambiguated_entity = candidates[0]  # This is a simplistic example
#         print(f"{ent.text} -> {disambiguated_entity}")

# 3. Contextual disambugation
def disambiguate_entity(entity, sentence):
    if entity.label_ == "ORG":
        if entity.text == "Apple":
            if "technology" in sentence or "iPhone" in sentence or "Cupertino" in sentence or "store" in sentence:
                return "Apple Inc."
            else:
                return "Apple"
        if entity.text == "Amazon":
            if "deforestation" in sentence or "rainforest" in sentence or "jungle" in sentence or "forest" in sentence:
                return "Amazon rainforest"
            else:
                return "Apple.com, Inc."
    # Add more rules for other entity types and cases
    return entity.text

for ent in doc.ents:
    disambiguated_entity = disambiguate_entity(ent, doc.text)
    query = query_wikipedia(disambiguated_entity)
    print(f"Original: {ent.text}, Disambiguated: {disambiguated_entity}, \n Query result: {query}")