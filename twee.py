import spacy
import string

# from berta import classify_yes_no_answers
from wiki import search_wikipedia, get_wikipedia_text

# Load the English language model
nlp = spacy.load('en_core_web_sm')

entity_list = {}
index_g = 0


def extract_entities(text, split_entity_words):
    # Process the text with spaCy
    doc = nlp(text)
    global index_g


    # Extract entities
    entities = [ent.text for ent in doc.ents]

    if(split_entity_words == 0):
        # Iterate through the words
        for word in entities.copy():
            if " " in word:
                # If the word contains a space, split and append the resulting words
                entities.remove(word)
                entities.extend(word.split())
    elif(split_entity_words == 1):
         for i in range(0, len(entities)):
            word = entities[i]
            if " " in entities[i]:
                # If the word contains a space, split and append the resulting words
                # entities.extend(word.split())
                # entities[i] = entities[i].replace(" ", "_").lower()
                entity_list[entities[i]] = str(index_g)
                entities[i] = "ENTITY_"+ str(index_g)
                index_g+=1


    return entities

def preprocess_text(text, split_entity_words):


    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Apply the translation table to remove punctuation
    cleaned_text = text.translate(translator)

    doc = nlp(cleaned_text)

    replaced_text = cleaned_text

    if(split_entity_words == 1):
        #Replace text for entities with space to underscore
        for ent in doc.ents:
            if " " in ent.text:
                # replaced_text = replaced_text.replace(ent.text, ent.text.replace(' ', '_'))
                if ent.text in entity_list:
                    # entities[i] = "ENTITY"+ entity_list[ent.text]
                    replaced_text = replaced_text.replace(ent.text, "ENTITY_"+ entity_list[ent.text])

    return replaced_text







def find_important_keywords(text, entities):
    q_nlp = nlp(text)
    # entities = [ent.text for ent in q_nlp.ents]
    # print("entities", entities)

    current_entiity = ""
    important_nouns = []
    important_adj = []
    important_verbs = []
    important_keywords = []

    temp_nouns = []
    temp_adj = []
    temp_verbs = []
    temp_keywords = []
    #Here I define the rule to conider when selecting important keywords
    for i in range(0, len(q_nlp)):
        token = q_nlp[i]
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

        # print( token.lemma_, token.pos_, token.is_stop)
        # if(token.is_stop):
        #     continue
        if(token.lemma_ in entities):
            if(len(temp_keywords) == 0):
                current_entiity = token.lemma_

            #This is for the case where the important keywords have not been associated to an entity
            elif(len(temp_keywords) != 0):
                if(current_entiity == "" ):
                    current_entiity = token.lemma_

                for noun in temp_nouns:
                    important_nouns.append([current_entiity, noun])

                for adj in temp_adj:
                    important_adj.append([current_entiity, adj])

                for verb in temp_verbs:
                    important_verbs.append([current_entiity, verb])

                #Reset the variables
                temp_nouns = []
                temp_adj = []
                temp_verbs = []
                temp_keywords = []

                #Setting current entity to new entity
                current_entiity = token.lemma_

        elif(token.pos_ == "NOUN" or token.pos_ == "PROPN"):
            important_keywords.append(token.lemma_)
            temp_keywords.append(token.lemma_)
            temp_nouns.append(token.lemma_)


        elif(token.pos_ == "ADJ"):
            important_keywords.append(token.lemma_)
            temp_keywords.append(token.lemma_)
            temp_adj.append(token.lemma_)


        elif(token.pos_ == "VERB"):
            important_keywords.append(token.lemma_)
            temp_keywords.append(token.lemma_)
            temp_verbs.append(token.lemma_)

    #This is for the case that only 1 entity appeared in the begining and all important keywords appeared later
    if(len(temp_keywords) != 0):
        current_entiity = token.lemma_

        for noun in temp_nouns:
            important_nouns.append([current_entiity, noun])

        for adj in temp_adj:
            important_adj.append([current_entiity, adj])

        for verb in temp_verbs:
            important_verbs.append([current_entiity, verb])


    important_information = {
        "NOUN" : important_nouns, 
        "ADJ"  : important_adj,
        "VERB" : important_verbs
    }

    # print("important_keywords", important_keywords)
    return important_keywords, important_information

def entity_linking(text, entities):
    prev_entity = ""
    current_entity = ""
    linked_entities = []
    temp_links = []

    t_nlp = nlp(text)

    for i in range(0, len(t_nlp)):
        token = t_nlp[i]
        if(token.lemma_ in entities):
            if(len(temp_links) > 0):
                for t in temp_links:
                    if(t[0]=="" ):
                        if(token.lemma_ != t[2]):
                            linked_entities.append([token.lemma_, t[1], t[2]])
                    else:
                        if(token.lemma_ != t[0]):
                            linked_entities.append([t[0], t[1], token.lemma_])

            prev_entity = current_entity
            current_entity = token.lemma_

        if(token.pos_ == "ADP"):
            if(prev_entity != current_entity):
                if(prev_entity == ""):
                    if(token.lemma_ == "from" or token.lemma_ == "of"):
                        temp_links.append([prev_entity, token.lemma_, current_entity])
                    else:
                        temp_links.append([current_entity, token.lemma_, prev_entity])

                elif(token.lemma_ == "from" or token.lemma_ == "of"):
                    linked_entities.append([prev_entity, token.lemma_, current_entity])
                else:
                    linked_entities.append([current_entity, token.lemma_, prev_entity])

    return linked_entities

                







question = "Is London the capital of The United Kingdom?"
llm_text = "London is from England which is the capital of The United Kingdom."
# llm_text = "London is located entirely within England."

question = "Is the Mona Lisa housed in the Louvre Museum?"
llm_text = "The Mona Lisa, housed within the Louvre Museum is a small painting (9 1/2 inches x 13 5/8) on wood. The artist used egg tempera for the background and added oil paint to the outline of his models face and hair. The painting was created in Florence around 1503. Leonardo Da Vinci completed this painting sometime between June of 1502 and May of 1504. It is a portrait of Lisa Gherardini, wife of wealthy Italian merchant Francesco del Giocondo. She looks mysterious as she stares out at the viewer of the picture. Da Vinci was a master of proportions in painting, and he used subtle facial expressions that give us a sense of her personality. The Mona Lisa has been housed at the Louvre since 1797, when "
# llm_text = "The Mona Lisa, everybody knows that da Vinci’s work is one of the greatest artpieces ever made."
# llm_text = "surely you are joking I'm sure I'm not the only one who thought of that famous quote from 'Catch 22'. But yes, it is. I know where it hangs! You know your geography.... Yep, I don't think the Louvre is in the same country as the Mona Lisa......  "

# question = question.lower()
# llm_text = llm_text.lower()

#Extract important keywords and entities from the question
entities = extract_entities(question, 0)
q_preprocessed_text = preprocess_text(question, 0)
important_keywords, important_information = find_important_keywords(q_preprocessed_text, entities)
linked_entities = entity_linking(q_preprocessed_text, entities)
print("entities", entities)

print("important_information", important_information)
print("important_keywords", important_keywords)
print("linked_entities", linked_entities)

# Extract important keywords and entities from the question
entities = extract_entities(llm_text, 1)
preprocessed_text = preprocess_text(llm_text, 0)
important_keywords, important_information = find_important_keywords(preprocessed_text, entities)
linked_entities = entity_linking(preprocessed_text, entities)

# print("entities2", entities)


# print("important_information2", important_information)
# print("important_keywords2", important_keywords)
# print("linked_entities2", linked_entities)