from berta import classify_yes_no_answers
from twee import *

from llama_cpp import Llama

model_path = "models/llama-2-7b.Q4_K_M.gguf"
# model_path = "models/llama-2-13b.Q4_K_M.gguf"
llm = Llama(model_path=model_path, verbose=False)

def get_questions():
    f = open("input.txt", "r")
    questions_num = []
    quesions = []

    for q in f: 
        question_words = q.split()
        questions_num.append(question_words[0])
        question_words.pop(0)
        quesions.append(' '.join(question_words))
    
    return questions_num, quesions


questions_num, questions = get_questions()

# output_file = open('output.txt', 'w')

i = 0
for question in questions:
    print(questions_num[i] + '     ' + question)   #REMOVE
    # output_file.write(questions_num[i] + '     ' + question +'\n')

    completion = llm(question)
    llm_text = completion['choices'][0]['text']

    print(questions_num[i] + '     R"' +llm_text+'"')   #REMOVE
    # output_file.write(questions_num[i] + '     R"' +llm_text+'"\n')

    tf,extracted_answer = classify_yes_no_answers(llm_text,question)
    if (extracted_answer == "Wiki") : print("Extracted answer: https://", extracted_answer)
    else : print(questions_num[i] + '     A"' +extracted_answer+'"')

    # We extract the information such entities links and important information(Nouns, Verbs and Adjectives)
    linked_entities, important_keywords, important_information, entities = extract_information_from_question(question)

    # We match the information such entities links and important information(Nouns, Verbs and Adjectives) of the question and 
    score = check_correctness(llm_text, linked_entities, important_information, entities)
    if(score >= 70):
        print(questions_num[i] + '     C' +'"correct"') #REMOVE
        # output_file.write(questions_num[i] + '     C' +'"correct"\n')
    else:
        print(questions_num[i] + '     C' +'"incorrect"') #REMOVE
        # output_file.write(questions_num[i] + '     C' +'"incorrect"\n')
        
    # handle_wiki_checking(entity_list, linked_entities, important_keywords, important_information, entities)
    parallelize_wiki_text_fetching(entity_list, important_keywords, linked_entities, entities)

    # del entity_list, linked_entities, important_keywords, important_information, entities
    i=i+1

# output_file.close()