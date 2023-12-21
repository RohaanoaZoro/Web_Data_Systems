from berta import classify_yes_no_answers

# from twee import extract_information_from_question
# from twee import check_correctness
# from twee import handle_wiki_checking

from twee import *

from llama_cpp import Llama

model_path = "models/llama-2-7b.Q4_K_M.gguf"
# model_path = "models/llama-2-13b.Q4_K_M.gguf"
llm = Llama(model_path=model_path, verbose=False)

prompts = [
    # "Is the population of Paris greater than 2 million?",
    # "Is Mount Everest the highest peak in the world?",
    # "Is Barack Obama listed as a Nobel Prize laureate?",
    # "Is the Eiffel Tower located in China?",
    # "Is the Mona Lisa housed in the Louvre Museum?",
    # "Is English the official language of the Netherlands?",
    # "Is Elon Musk the CEO of Microsoft?",
    # "Is the Pacific Ocean the largest ocean on Earth?",
    # 'Is "The Great Gatsby" written by F. Scott Fitzgerald?',
    # 'Is the Statue of Liberty located in London?'
    "Is London the capital of The United Kingdom?",
    'Question: What is the capital of Germany?'
]

for prompt in prompts:
    print("Input (A): ", prompt)

    completion = llm(prompt)
    llm_text = completion['choices'][0]['text']
    print("Text returned by the language model (B) (llama 2, 7B): ", llm_text)

    tf,extracted_answer = classify_yes_no_answers(llm_text,prompt)
    if (extracted_answer == "Wiki") : print("Extracted answer: https://", extracted_answer)
    else : print("Extracted answer: ", extracted_answer)

    # We extract the information such entities links and important information(Nouns, Verbs and Adjectives)
    linked_entities, important_keywords, important_information, entities = extract_information_from_question(prompt)

    # We match the information such entities links and important information(Nouns, Verbs and Adjectives) of the question and 
    score = check_correctness(llm_text, linked_entities, important_information, entities)
    if(score >= 70):
        # print("Part 3: Correct", score)
        print('Correctness of the answer: "correct"')
    else:
        print('Correctness of the answer: "incorrect"')
        # print("Part 3: Incorrect", score)
        
    # handle_wiki_checking(entity_list, linked_entities, important_keywords, important_information, entities)

    