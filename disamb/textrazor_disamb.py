import textrazor

textrazor.api_key = "bef32bcb5da32fda5e41f53e60ac09689f3e05e6c67bfed90ab515f7"

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze("Deforestation in Brazil’s Amazon rainforest reached a record high for the first six months of the year, as an area five times the size of New York City was destroyed, preliminary government data showed on Friday.")

for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score)