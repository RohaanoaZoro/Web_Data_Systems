import spacy
import string
import re

from berta import classify_yes_no_answers
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
                temp_split = word.split()

                filtered_list = [word for word in temp_split if word.lower() not in set(nlp.Defaults.stop_words)]
                
                entities.extend(filtered_list)
                
    elif(split_entity_words == 1):
         for i in range(0, len(entities)):
            word = entities[i]
            if " " in entities[i]:
                # If the word contains a space, split and append the resulting words
                # entities.extend(word.split())
                # entities[i] = entities[i].replace(" ", "_").lower()
                if(entities[i] not in entity_list):
                    entity_list[entities[i]] = str(index_g)
                    entities[i] = "ENTITY_"+ str(index_g)
                    index_g+=1
                else:
                    entities[i] = "ENTITY_"+ entity_list[entities[i]]
    return entities


def preprocess_text(text, split_entity_words):
    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Apply the translation table to remove punctuation
    cleaned_text = text.translate(translator)
    pattern = re.compile(r'\([^)]*\)')
    # Replace matches with a space
    modified_text = pattern.sub(' ', cleaned_text)
    replaced_text = cleaned_text
    doc = nlp(replaced_text)

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
        elif(token.pos_ == "ADP"):
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


def check_entity_links(linked_entities1, linked_entities2):
    # print("hello",linked_entities1, linked_entities2)
    matched_links = []
    for links in linked_entities1:
        for links2 in linked_entities2:
            # print("links", links, links2)
            if(links[0] == links2[0] and links[2] == links2[2]):
                matched_links.append(links)

    return matched_links


def check_keyword_matches(important_information1, important_information2):
    matched_nouns = []
    matched_adj = []
    matched_verbs = []
    # print("important_information1", important_information1)
    # print("important_information2", important_information2)

    for imp1 in important_information1["NOUN"]:
         for imp2 in important_information2["NOUN"]:
            if(imp1[0] == imp1[0] and imp2[1] == imp2[1]):
                matched_nouns.append(imp1)

    for imp1 in important_information1["ADJ"]:
         for imp2 in important_information2["ADJ"]:
            if(imp1[0] == imp1[0] and imp2[1] == imp2[1]):
                matched_adj.append(imp1)

    for imp1 in important_information1["VERB"]:
        for imp2 in important_information2["VERB"]:
            if(imp1[0] == imp1[0] and imp2[1] == imp2[1]):
                matched_verbs.append(imp1)

    return matched_nouns, matched_adj, matched_verbs


def calculate_score(matched_links, linked_entities, matched_nouns, matched_adj, matched_verbs, important_information, entities, entities2):
    score = 100
    # print("matched_links", matched_links, linked_entities)
    if(len(matched_links) < len(linked_entities)):
        score -= int((len(linked_entities) - len(matched_links)) / len(linked_entities))*50
        # print("Reason: Important Entities missing ", matched_links, linked_entities)

    elif(len(linked_entities) == 0):
        unique_to_list = list(set(entities) - set(entities2))
        if(len(unique_to_list) > 0):
            score -= (len(unique_to_list)/len(entities)) * 50
            # print("Reason: Important Entities missing ", unique_to_list)


    if(len(matched_nouns) < len(important_information["NOUN"])):
        score -= int((len(important_information["NOUN"]) - len(matched_nouns)) / len(important_information["NOUN"]))*20
        # print("Reason: Important Nouns missing ", matched_nouns, important_information["NOUN"])


    if(len(matched_adj) < len(important_information["ADJ"])):
        score -= int((len(important_information["ADJ"]) - len(matched_adj)) / len(important_information["ADJ"]))*10
        # print("Reason: Important ADJ missing ", matched_adj, important_information["ADJ"])


    if(len(matched_verbs) < len(important_information["VERB"])):
        score -= int((len(important_information["VERB"]) - len(matched_verbs)) / len(important_information["VERB"]))*20
        # print("Reason: Important VERBS missing ", matched_verbs, important_information["VERB"])

    return score


def extract_information_from_question(text):
    #Extract important keywords and entities from the question
    entities = extract_entities(text, 1)
    q_preprocessed_text = preprocess_text(text, 1)
    important_keywords, important_information = find_important_keywords(q_preprocessed_text, entities)
    linked_entities = entity_linking(q_preprocessed_text, entities)

    return linked_entities, important_information, important_information, entities


def check_correctness(llm_text, linked_entities, important_information, entities):
    # Extract important keywords and entities from the question
    entities2 = extract_entities(llm_text, 1)
    preprocessed_text2 = preprocess_text(llm_text, 1)
    important_keywords2, important_information2 = find_important_keywords(preprocessed_text2, entities2)
    linked_entities2 = entity_linking(preprocessed_text2, entities2)

    # print("entities2", entities2)
    # print("important_information2", important_information2)
    # print("important_keywords2", important_keywords2)
    # print("linked_entities2", linked_entities2)

    matched_links = check_entity_links(linked_entities, linked_entities2)
    # print("matched_links", matched_links)
    # print("Check", len(matched_links), len(linked_entities))

    matched_nouns, matched_adj, matched_verbs = check_keyword_matches(important_information, important_information2)
    # print("Check Noun", len(matched_nouns), len(important_information["NOUN"]))
    # print("Check ADJ", len(matched_adj), len(important_information["ADJ"]))
    # print("Check Verb", len(matched_verbs), len(important_information["VERB"]))

    score = calculate_score(matched_links, linked_entities, matched_nouns, matched_adj, matched_verbs, important_information, entities, entities2)

    return score


def check_correctness2(llm_text, linked_entities, important_information, entities):
    # Extract important keywords and entities from the question
    entities2 = extract_entities(llm_text, 1)
    preprocessed_text2 = preprocess_text(llm_text, 1)
    important_keywords2, important_information2 = find_important_keywords(preprocessed_text2, entities2)
    linked_entities2 = entity_linking(preprocessed_text2, entities2)

    # print("entities2", entities2)
    # print("important_information2", important_information2)
    # print("important_keywords2", important_keywords2)
    # print("linked_entities2", linked_entities2)

    matched_links = check_entity_links(linked_entities, linked_entities2)
    print("matched_links", matched_links)
    print("Check", len(matched_links), len(linked_entities))

    matched_nouns, matched_adj, matched_verbs = check_keyword_matches(important_information, important_information2)
    print("Check Noun", len(matched_nouns), len(important_information["NOUN"]))
    print("Check ADJ", len(matched_adj), len(important_information["ADJ"]))
    print("Check Verb", len(matched_verbs), len(important_information["VERB"]))

    score = calculate_score(matched_links, linked_entities, matched_nouns, matched_adj, matched_verbs, important_information, entities, entities2)

    return score


def handle_wiki_checking(entity_list, linked_entities, important_keywords, important_information, entities):

    print(entity_list)  #REMOVE

    wiki_search_results = search_wikipedia(entity_list, important_keywords)
    my_wiki_urls = []
    # my_wiki_entities = []

    print("Entities extracted: ")

    for result in wiki_search_results:
        print(f"URL: {result['url']}")  #REMOVE
        # print(result)  #REMOVE

        # We get wiki text from wikipedia
        wiki_paras = get_wikipedia_text(result['url'], 10)

        score_arr = []
        for wiki_para in wiki_paras[:10]:
            # We match the information such entities links and important information(Nouns, Verbs and Adjectives) of the question and 
            score = check_correctness(wiki_para, linked_entities, important_information, entities)
            score_arr.append(score)

            # print("score XXX", score)
            if(score >= 70):
                my_wiki_urls.append(result['url'])
                # my_wiki_entities
                # break

        print("score_arr", score_arr)

    print("Part 4: my_wiki_urls", my_wiki_urls)  #REMOVE


    






# question = "Is London the capital of The United Kingdom?"
# llm_text = "London is from England which is the capital of the United Kingdom."
# # llm_text = "London is located entirely within England."

# # question = "Is The Mona Lisa housed in the Louvre Museum?"
# # # # question = "Did my cousin Mona Lisa go to the Louvre Museum?"
# # # llm_text = "The Mona Lisa, housed within the Louvre Museum is a small painting (9 1/2 inches x 13 5/8) on wood. The artist used egg tempera for the background and added oil paint to the outline of his models face and hair. The painting was created in Florence around 1503. Leonardo Da Vinci completed this painting sometime between June of 1502 and May of 1504. It is a portrait of Lisa Gherardini, wife of wealthy Italian merchant Francesco del Giocondo. She looks mysterious as she stares out at the viewer of the picture. Da Vinci was a master of proportions in painting, and he used subtle facial expressions that give us a sense of her personality. The Mona Lisa has been housed at the Louvre since 1797, when "
# # # # llm_text = "The Mona Lisa, everybody knows that da Vinci’s work is one of the greatest artpieces ever made."

# # # llm_text = "surely you are joking I'm sure I'm not the only one who thought of that famous quote from 'Catch 22'. But yes, it is. I know where it hangs! You know your geography.... Yep, I don't think the Louvre is in the same country as the Mona Lisa......  "
# # # llm_text = "The Louvre (English/ LOOV(-rə)),[4] or the Louvre Museum (French: Musée du Louvre [myze dy luvʁ] ⓘ), is a national art museum in Paris, France. It is located on the Right Bank of the Seine in the city's 1st arrondissement (district or ward) and home to some of the most canonical works of Western art, including the Mona Lisa and the Venus de Milo. The museum is housed in the Louvre Palace, originally built in the late 12th to 13th century under Philip II. Remnants of the Medieval Louvre fortress are visible in the basement of the museum. Due to urban expansion, the fortress eventually lost its defensive function, and in 1546 Francis I converted it into the primary residence of the French Kings.[5]"
# # # # llm_text = "The Louvre English ˈluːvrə LOOVrə4 or the Louvre Museum French Musée du Louvre myze dy luvʁ ⓘ is a national art museum in Paris France It is located on ENTITY_2 in the citys 1st arrondissement district or ward and home to some of the most canonical works of Western art including the Mona Lisa and ENTITY_3 The museum is housed in the Louvre Palace originally built in ENTITY_5 under Philip II Remnants of the Medieval Louvre fortress are visible in the basement of the museum Due to urban expansion the fortress eventually lost its defensive function and in 1546 Francis I converted it into the primary residence of the French Kings5"
# # # # question = "Is Elon Musk the CEO of Microsoft?"
# # # llm_text = "nobody can be sure, but it seems a high probability that he will. this is how it will happen: 1- Microsoft buys Tesla for 7 billion $. 2- Musk becomes VP for Artificial Intelligence at Microsoft. 3- Musk starts to promote AI as the future, and in fact, the only way to survive on earth. 4- Musk talks about the singularity and why it is the only way out. 5- Musk says that the time left until the singularity has begun are few days or weeks at most, and that we have no other option but to accept this. 6- All people who don't agree with his statements will be considered AI-haters , and will be punished as such by being removed from the society and any rights they might have had so far. 7- People will start to complain about the censorship, but Microsoft will defend itself saying that is in accordance with the law against hate speech. 8- Any further discussion regarding the singularity will be considered AI-hate speech and will result in punishment for all involved parties, including the death penalty for Musk himself. 9"
# # # # llm_text = "Bill Gates is the CEO of Microsoft"

# # question = "Was there significant imporvement in Amazon deforestation?"
# # llm_text = "As of 2023, there has been a significant reduction in Amazon deforestation. As of April 2023, Amazon deforestation was down 68% compared to the previous year, with 127 square miles of forest having been destroyed. This figure is notably below the historic April average of 176 square miles​​."


# answer, strzz = classify_yes_no_answers(llm_text)
# print("Part 2: ", answer, strzz)

# #We extract the information such entities links and important information(Nouns, Verbs and Adjectives)
# linked_entities, important_keywords, important_information, entities = extract_information_from_question(question)

# #We match the information such entities links and important information(Nouns, Verbs and Adjectives) of the question and 
# score = check_correctness(llm_text, linked_entities, important_information, entities)
# if(score >= 70):
#     print("Part 3: Correct", score)
# else:
#     print("Part 3: Incorrect", score)

# handle_wiki_checking(entity_list, linked_entities, important_keywords, important_information, entities)

# # wiki_para = "The population of the United Kingdom was estimated at over 67.0 million in 2020. It is the 21st most populated country in the world and has a population density of 270 people per square kilometre (700 people/sq mi), with England having significantly greater density than Wales, Scotland, and Northern Ireland.[3] Almost a third of the population lives in south east England, which is predominantly urban and suburban, with about 9 million in the capital city, London, whose population density is just over 5,200 per square kilometre (13,468 per sq mi).[4]"

# #  #We match the information such entities links and important information(Nouns, Verbs and Adjectives) of the question and 
# # score = check_correctness(wiki_para, linked_entities, important_information, entities)
# # print("score XXX", score)
