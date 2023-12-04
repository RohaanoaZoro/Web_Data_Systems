import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')


def extract_entities(text, split_entity_words):
    # Process the text with spaCy
    doc = nlp(text)

    # Extract entities
    entities = [ent.text for ent in doc.ents]

    if(split_entity_words):
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
    q_entities = extract_entities(question, True)
    llm_entities = extract_entities(llm_text, True)

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

def answer_yes_no_questions(question, llm_text):
    missing_words = find_words_not_present_in_question(question, llm_text)
    # print("missing_words", missing_words)

    important_keywords = find_important_keywords(question)
    # important_keywords.append(" ")
    # print("important_keywords", important_keywords)

    unique_missing_words = list(set(missing_words) - set(important_keywords))
    # print("unique_missing_words", unique_missing_words)

    #ToDO
    # Word order to check if something is true. Italy is the capial of Rome?
    # Negation not
    yes_no_answer = verify_with_yes_no_for_question(missing_words, important_keywords)

def answer_what_questions(question, llm_text):
    missing_words = find_words_not_present_in_question(question, llm_text)
    print("missing_words", missing_words)
    q_entities = extract_entities(question, False)
    print("q_entities", q_entities)

    # extract_answer_what(llm_text, q_entities)
    subject, verb, entity = extract_subject_verb_entity(question)
    print("Subject:", subject)
    print("Verb:", verb)
    print("Entity:", entity)

    extract_answer_what(llm_text, subject, verb, entity, q_entities)



def extract_answer_what(llm_text, subject, verb, entity, q_entities):
    llm_sentences = [sentence.text for sentence in nlp(llm_text).sents]

    subject_pos = -1
    verb_pos = -1
    entitiy_pos = -1

    possible_answers = []

    for sentence in llm_sentences:
        nlp_sentence = nlp(sentence)

        current_pos = 0
        for token in nlp_sentence:
            if(len(subject)> 0 and token.lemma_ in subject):
                subject_pos = current_pos

            if(token.pos_ == "VERB" and token.lemma_ in verb):
                verb_pos = current_pos

            if(token.lemma_ in entity or token.lemma_ in q_entities):
                entitiy_pos = current_pos

            # print(token.pos_, token.lemma_)
            if(token.pos_ == "ADP"):
                for i in range(current_pos+1, len(nlp_sentence)):
                    temp_token = nlp_sentence[i]
                    if(temp_token.pos_ == "NOUN" or temp_token.pos_ == "PROPN" or temp_token.pos_ == "NUM"):
                        possible_answers.append(temp_token.lemma_)
                    else:
                        break
                    

                    

            current_pos+=1


    print("possible_answers", possible_answers)
    return possible_answers




def extract_question_what(question, q_entities):

    what_pos = -1
    subject_pos = -1


    keywords_to_lookfor = []
    nlp_question = nlp(question)
    current_index = 0
    for token in nlp_question:
        if(token.lemma_ == "what"):
            what_pos = current_index

        if(token.pos_ == "ADP" and search_pos != -1):
            keywords_to_lookfor.append(token.lemma_)
            search_pos = current_index



        #This means that we have found the what and need to 
        if((token.pos_ == "ADJ" or token.pos_ == "NOUN" or token.pos_ == "PROPN") and what_pos != -1):
            keywords_to_lookfor.append(token.lemma_)
            search_pos = current_index



        current_index+=1

def extract_subject_verb_entity(question):
    doc = nlp(question)

    subject = []
    verb = []
    entity = []

    for token in doc:
        if token.dep_ == "nsubj":
            subject.append(token.text)
        elif token.pos_ == "VERB":
            verb.append(token.text)
        elif "obj" in token.dep_:
            entity.append(token.text)

    return subject, verb, entity








question="What is the height of the Burj Khalifa?"
llm_text = "The buildings are 862 meters tall. How tall can a tree get? (height vs diameter) The World’s Tallest Building – Burj Khalifa -2016 What is the World's Highest Skyscraper? Burj Khalifa - World's Tallest Tower | Documentary 1080p HD What Is The World's Fastest Elevator? The World’s 5 Best Skyscrapers (& The Biggest Skyscraper Mistakes) "

# This Works
# question = "Is London the capital of The United Kingdom?"
# llm_text = "London is in England which is the capital of The United Kingdom."
# llm_text = "London is located entirely within England."

# This Works
question = "Is the Mona Lisa housed in the Louvre Museum?"
# llm_text = "The Mona Lisa, housed within the Louvre Museum, is a small painting (9 1/2 inches x 13 5/8) on wood. The artist used egg tempera for the background and added oil paint to the outline of his models face and hair. The painting was created in Florence around 1503. Leonardo Da Vinci completed this painting sometime between June of 1502 and May of 1504. It is a portrait of Lisa Gherardini, wife of wealthy Italian merchant Francesco del Giocondo. She looks mysterious as she stares out at the viewer of the picture. Da Vinci was a master of proportions in painting, and he used subtle facial expressions that give us a sense of her personality. The Mona Lisa has been housed at the Louvre since 1797, when "
# llm_text = "The Mona Lisa, everybody knows that da Vinci’s work is one of the greatest artpieces ever made."
llm_text = "surely you are joking I'm sure I'm not the only one who thought of that famous quote from 'Catch 22'. But yes, it is. I know where it hangs! You know your geography.... Yep, I don't think the Louvre is in the same country as the Mona Lisa......  "

# question = "Is Rome the capital of Italy?"
# llm_text = "Milan is the second largest and most populated city in italy, but it's not the capital city. The capital city is Rome."
# llm_text = "London is located entirely within England."

# question = "Is Elon Musk the CEO of Microsoft?"
# llm_text = "nobody can be sure, but it seems a high probability that he will. this is how it will happen: 1- Microsoft buys Tesla for 7 billion $. 2- Musk becomes VP for Artificial Intelligence at Microsoft. 3- Musk starts to promote AI as the future, and in fact, the only way to survive on earth. 4- Musk talks about the singularity and why it is the only way out. 5- Musk says that the time left until the singularity has begun are few days or weeks at most, and that we have no other option but to accept this. 6- All people who don't agree with his statements will be considered AI-haters , and will be punished as such by being removed from the society and any rights they might have had so far. 7- People will start to complain about the censorship, but Microsoft will defend itself saying that is in accordance with the law against hate speech. 8- Any further discussion regarding the singularity will be considered AI-hate speech and will result in punishment for all involved parties, including the death penalty for Musk himself. 9"
# llm_text = "Bill Gates is the CEO of Microsoft"

# question = "What is Albert Einstein's birth date?"
# # llm_text = "Albert Einstein's birth certificate shows that he was born in 14 March, but this date has never been authenticated by the German government, and some experts have suggested an alternative date based on his parents' marriage certificate.[23] This claim is disputed;[24] in any case, it remains unclear which of these dates—if either—is correct. What is the birthdate of Albert Einstein? The birthday of the famous scientist is unknown."
# llm_text = "Albert Einstein's birth certificate shows that he was born on 14 March,"
# llm_text = "Albert Einstein was born at Ulm, in Württemberg, Germany, on March 14, 1879."


# question = "What is the chemical formula for water?"
# llm_text = "explains water as H2O. It has two atoms (in this case, hydrogen) and one oxygen atom. If you were asked to write out a formula showing the number of each type of atom in a molecule or compound, you would first list its name. You might remember that water is composed of 2 parts hydrogen and 1 part oxygen. If you have ever seen an equation, then you know that you can use this information to create a formula for writing out the elements in a formula."


# question = "Is the Netherlands in Germany?"
# llm_text = "nobody likes to be reminded of this. So I guess the Germans don't either. They prefer to think that their country is so big and multi-faceted, that they simply can’t be held responsible for what happens in other parts of their country, particularly when those parts are in another EU member state. But the facts speak for themselves. After the Nazi period of terror from 1938 to 1945, Germany was stripped of all its colonies including Alsace-Lorraine and East Prussia, which were handed over to France and Poland respectively. In their place, in addition to taking control of large swathes of the east, West Germany got the Saarland, an area ceded from France between 1920-75. But this wasn’t enough for Chancellor Konrad Adenauer, who had a dream of creating an “German Empire” (Reich) extending from the Rhine to the Donets and Oder rivers, which are today shared by Germany, Poland, Austria, Switzerland, France, Ukraine, Slovakia, Czech Republic, Hungary, Moldova, Romania, Belarus. "


# question = "Is Amsterdam in The Netherlands?"
# llm_text = "Amsterdam is the Netherlands’ capital, known for its artistic heritage, elaborate canal system and narrow houses with gabled facades, legacies of the city’s 17th-century Golden Age. Its Museum District houses the Van Gogh Museum, works by Rembrandt and Vermeer at the Rijksmuseum, and modern art at the Stedelijk. Cycling is key to the city’s character, and there are numerous bike paths. "
# llm_text = "surely not! the capital of Holland is The Hague. but Amsterdam is also a major city and quite often tourists get confused because they are looking for information about the country, not just one city within it. so…what’s the deal? if you ask people to point out on a map where the Netherlands is located, most likely they will doze off or become extremely confused. Is Amsterdam In The Netherlands: A Short Answer To This Frequently Asked Question The answer to this question is not always straightforward due to the fact that many people don’t know exactly what constitutes a “country,” and what defines an “island.” However, if you look at it from a geographic standpoint, Amsterdam is located in The Netherlands because it lies within the bordered area that makes up Europe. In addition, it borders water on all sides which qualifies it as part of this continent’s land mass. There are many reasons why someone might want to know if Amsterdam is in The Netherlands or not. For example, some people may simply be curious about where their home country falls within the world map while others could have an interest in learning more about different countries around them so they can plan future traveling plans accordingly!"

# question = "Is University of Amsterdam in London?"
# llm_text = "It is a branch of the University of Amsterdam (UvA) that is based on the British campus. The university also runs branches in Barcelona and São Paulo. UvA College London has an internationally recognized research focus, which attracts researchers from all over the world."

# question = "Is Vrije University Amsterdam in London?"
# llm_text = " surely not. I don't know why this has to be answered all the time, but it is not a location of any university. The same goes for Leiden University and Utrecht University. I would like to know if there are universities for international students in the following countries: 1) Amsterdam (Netherlands), 2) Rotterdam (Netherlands), 3) Vienna (Austria), 4) Berlin (Germany) If not, is it possible to study in the Netherlands?"


# question = "Who painted the Mona Lisa?"
# llm_text = "The true identity of the Mona Lisa has not been discovered. However, there are theories that the portrait could be a self-portrait of Leonardo da Vinci himself. In recent years, some people have claimed to have found clues suggesting this theory may be correct, but so far none of these claims has been substantiated."

# question = "Is Real Madrid the best team in the world?"
# llm_text = "everybody is saying they are the best team in the world. But there's no way they are even as good as Messi-Neymar-Suarez. They may be a great team but they have no competition with that trio at Barca. You're right, Real Madrid is not the best team in the world. I think Messi and his pals are better than all teams except Bayern Munich."

# question = "What do spanish people eat?"
# llm_text = "Spanish cuisine is the result of a mixture between different peoples’ customs and influences, so that we can find dishes from all over Europe. But it should be noted that the Mediterranean diet has been the most important influence in the history of Spanish gastronomy: rich in fish and vegetables, this cuisine is healthy and light, even though it’s very tasty too! Spanish main dishes are usually made from rice, potatoes, pulses and a piece of meat. In Spain there are many regional specialities, like the Catalan paella (made up of saffron, peas, meat and seafood) or the Riojan suckling pig. But apart from these special dishes that people usually eat on holidays, most Spanish recipes are very easy to prepare: for instance a Spanish tortilla de patatas is made with potatoes, beaten eggs and olive oil. And many other recipes can be found in this website: Spain Cookbook Spanish desserts are delicious: caramel custard (called flan), apple or pear pie and cinnamon rolls are our"

# question = "Do chicas like paella?"
# llm_text = "I'd venture that they do not.♠ In my experience, and in keeping with my general observation regarding the nature of women; they don't give a shit what you cook (for them), as long as it is edible, nutritious, and reasonably tasty. In this case, 'reasonably' does NOT necessarily imply 'excellent'. Now, there are some who would object to my description of paella as 'edible', but I am not one of those people. I've had it in Spain, and it was good. My only complaint was that the rice seemed too much like a mushroom; it didn't have that slightly crunchy, chewy texture to it that would make me wander off into the kitchen to hunt down the cook. The rice should be firm enough to hold up its end against the other ingredients in the dish, but not so much as to overwhelm them and their flavors. If you can't get a decent rice on it, don't bother with it. I've had it in other countries (Mexico, Portugal, Italy), and the results were similar. I'm"

# question = "Is English the official language of the Netherlands?"
# llm_text = " surely not, there are a lot off languages in the NL. For example it is mandatory at schools for kids to learn one of those other than Dutch (usually German or French), but I don't know if this is still active in all schools. @DennisDennis: I am aware that Dutch isn’t the only official language in the Netherlands, but English is an official language under international law and its use has been encouraged by the EU for decades. Even though the rules have relaxed considerably over time, I think it still applies. I disagree with the 'too hard' part. It's not too hard to learn one more language or even two if you want to. @Kris: You may need to be a bit creative in your approach but that shouldn’t make learning English any harder than other languages. I can think of many non-English speakers who have learned at least some English through movies and music. It is also possible to learn from websites, books and other online resources. @Kris: What you say about learning the Dutch language doesn't apply here. English isn't as hard for us because we can use Google Translate,  unique_to_list ['?']"

question = "the capital of Nicaragua is"
llm_text = "Prior to 1979, Nicaragua was known as the Republic of Nicaragua. It is a republic with a presidential system of government. The capital of Nicaragua is Managua. The capital of Nicaragua is Managua."
llm_text = "Nicaragua, officially the Republic of Nicaragua (Spanish: República de Nicaraguaⓘ), is the largest country in Central America, bordered by Honduras to the north, the Caribbean to the east, Costa Rica to the south, and the Pacific Ocean to the west. Managua is the country's capital and largest city. As of 2015, it was estimated to be the third largest city in Central America. Nicaragua's multiethnic population of six million includes people of mestizo, Indigenous, European and African heritage. The main language is Spanish. Indigenous tribes on the Mosquito Coast speak their own languages and English. "

# question = "What is the capital of Nicaragua?"
# llm_text = "Managua is the capital of Nicaragua. What is the capital of Nicaragua and its population? Managua is the capital of Nicaragua. The population of Managua is 1.3 million people. Is Managua the capital"
question = question.lower()
llm_text = llm_text.lower()

llm_sentences = [sentence.text for sentence in nlp(llm_text).sents]

question_nlp = nlp(question)    
print(question)

for token in question_nlp:
    print(token.lemma_, token.pos_)


for sentence in llm_sentences:
    #We extract the nlp information from each sentence e.g POS tags, lemma, etc
    sentence_nlp = nlp(sentence)    
    print(sentence)

    for token2 in sentence_nlp:
        print(token2.lemma_, token2.pos_)

    break


        


# answer_yes_no_questions(question, llm_text)
answer_what_questions(question, llm_text)