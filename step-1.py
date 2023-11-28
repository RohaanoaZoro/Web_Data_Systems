import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')


def extract_entities(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Extract entities
    entities = [ent.text for ent in doc.ents]

    # Iterate through the words
    for word in entities.copy():
        if " " in word:
            # If the word contains a space, split and append the resulting words
            entities.remove(word)
            entities.extend(word.split())

    return entities

def find_words_not_present_in_question(question, llm_text):

    #We extract the nlp information
    question_nlp = nlp(question)
    llm_nlp = nlp(llm_text)

    #We use spacy to split the text into sentences
    llm_sentences = [sentence.text for sentence in llm_nlp.sents]

    #We create the list of words in the question
    question_words = [token.lemma_ for token in question_nlp if not token.is_stop]

    common_words=[]
    possibly_common_words = []
    for sentence in llm_sentences:
        # print(sentence)

        #We extract the nlp information from each sentence e.g POS tags, lemma, etc
        sentence_nlp = nlp(sentence)    

        for token in question_nlp:
            for token2 in sentence_nlp:

                #We check if in a sentence the POS tag and the lemma match
                
                if(token.pos_ == token2.pos_ and token2.lemma_ == token.lemma_ and not token.is_stop):
                    # print(token.pos_, token.lemma_)
                    common_words.append(token.lemma_)
                elif(token2.lemma_ == token.lemma_ and not token.is_stop):
                    possibly_common_words.append(token.lemma_)
        
        # print("common_words", common_words)

    unique_to_list = list(set(question_words) - set(common_words) - set(possibly_common_words))
    print("unique_to_list", unique_to_list)

    return unique_to_list

def check_missing_entities(q_entities, missing_words):
    # print("q_entities", q_entities)
    # print("missing_words", missing_words)
    missing_entities = [entity for entity in q_entities if entity in missing_words]
    # print("missing_entities", missing_entities)
    
    return missing_entities

def check_important_words(llm_text, important_words):
    llm_words = [keyword.lemma_ for keyword in nlp(llm_text)]
    important_keywords = [keyword for keyword in important_words if keyword not in llm_words]
    return important_keywords



def check_missing_nouns(missing_words):
    missing_nouns = []
    temp = " ".join([word for word in missing_words])
    missing_nlp = nlp(temp)
    for token in missing_nlp:
        if(token.pos_ == "NOUN" or token.pos_ == "PROPN"):
            missing_nouns.append(token.lemma_)
        # print("X", token.pos_, token.lemma_)

    return missing_nouns

def find_important_keywords(question):
    q_nlp = nlp(question)
    entities = [ent.text for ent in q_nlp.ents]
    # print("entities", entities)

    current_entiity = ""
    important_keywords = []
    #Here I define the rule to conider when selecting important keywords
    for i in range(0, len(q_nlp)):
        token = q_nlp[i]
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
        if(current_entiity != ""):
            if(token.pos_ == "NOUN" or token.pos_ == "PROPN" or token.pos_ == "ADJ"):
                important_keywords.append(token.lemma_)
                current_entiity = ""
        elif(token.lemma_ in entities):
            # print("In Entity #########")
            current_entiity = token.lemma_

    # print("important_keywords", important_keywords)
    return important_keywords


def verify_with_yes_no_for_question(missing_words, important_words):
    q_entities = extract_entities(question)
    llm_entities = extract_entities(llm_text)

    missing_enitities = check_missing_entities(q_entities, missing_words)

    if(len(missing_enitities) == 0):
        missing_nouns = check_missing_nouns(missing_words)

        important_keywords = check_important_words(llm_text, important_words)
        if(len(missing_nouns) != 0):
            print("No, Due to missing nouns such as", missing_nouns)
            return
        if(len(important_keywords)!= 0):
            print("No, Due to missing important keywords such as", important_keywords)
            return

        print("Yes, This is the answer the question", missing_nouns, important_keywords)

        # *******Handle not negation************
    
    else:
        print("No, Due to missing entities this is not the answer", missing_enitities)

# question="What is the height of the Burj Khalifa?"
# llm_text = "The buildings are 862 meters tall. How tall can a tree get? (height vs diameter) The World’s Tallest Building – Burj Khalifa -2016 What is the World's Highest Skyscraper? Burj Khalifa - World's Tallest Tower | Documentary 1080p HD What Is The World's Fastest Elevator? The World’s 5 Best Skyscrapers (& The Biggest Skyscraper Mistakes) "

# This Works
question = "Is London the capital of The United Kingdom?"
llm_text = "London is in England which is the capital of The United Kingdom."
# llm_text = "London is located entirely within England."

# This Works
question = "Is the Mona Lisa housed in the Louvre Museum?"
llm_text = "The Mona Lisa, housed within the Louvre Museum, is a small painting (9 1/2 inches x 13 5/8) on wood. The artist used egg tempera for the background and added oil paint to the outline of his models face and hair. The painting was created in Florence around 1503. Leonardo Da Vinci completed this painting sometime between June of 1502 and May of 1504. It is a portrait of Lisa Gherardini, wife of wealthy Italian merchant Francesco del Giocondo. She looks mysterious as she stares out at the viewer of the picture. Da Vinci was a master of proportions in painting, and he used subtle facial expressions that give us a sense of her personality. The Mona Lisa has been housed at the Louvre since 1797, when "
# llm_text = "The Mona Lisa, everybody knows that da Vinci’s work is one of the greatest artpieces ever made."

# question = "Is Rome the capital of Italy?"
# llm_text = "Milan is the second largest and most populated city in italy, but it's not the capital city. The capital city is Rome."
# llm_text = "London is located entirely within England."

question = question.lower()
llm_text = llm_text.lower()

missing_words = find_words_not_present_in_question(question, llm_text)
# print("missing_words", missing_words)

important_keywords = find_important_keywords(question)
# important_keywords.append(" ")
# print("important_keywords", important_keywords)

unique_missing_words = list(set(missing_words) - set(important_keywords))
# print("unique_missing_words", unique_missing_words)


yes_no_answer = verify_with_yes_no_for_question(missing_words, important_keywords)