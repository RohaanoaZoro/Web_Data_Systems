import requests

def get_rdf_for_entity_in_english(entity):
    # Construct the SPARQL query to fetch RDF triples for the specified entity in English
    sparql_query = f"""
    CONSTRUCT {{
        <http://dbpedia.org/resource/{entity}> ?p ?o.
    }}
    WHERE {{
        <http://dbpedia.org/resource/{entity}> ?p ?o.
        FILTER(LANG(?o) = 'en')
    }}
    """

    # DBpedia SPARQL endpoint
    endpoint_url = "http://dbpedia.org/sparql"

    # Set the headers for the request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'application/rdf+xml',  # Specify RDF/XML as the response format
    }

    # Set the parameters for the request
    params = {
        'query': sparql_query,
        'format': 'application/rdf+xml'
    }

    try:
        # Make the SPARQL request to DBpedia with headers
        response = requests.get(endpoint_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Get the RDF content
        rdf_content = response.text

        # Output the RDF content
        print(f"RDF content in English for {entity}:\n{rdf_content}")

        return rdf_content
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
entity = "Barack_Obama"
rdf_content = get_rdf_for_entity_in_english(entity)

# Now, you can process the RDF content as needed
# ...
