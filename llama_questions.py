from ctransformers import AutoModelForCausalLM
from step import *

repository = "TheBloke/Llama-2-7B-GGUF"
model_file = "llama-2-7b.Q4_K_M.gguf"
llm = AutoModelForCausalLM.from_pretrained(repository, model_file=model_file, model_type="llama")

prompts = [
    "Is the population of Paris greater than 2 million?",
    "Is Mount Everest the highest peak in the world?",
    "Is Barack Obama listed as a Nobel Prize laureate?",
    "Is the Eiffel Tower located in China?",
    "Is the Mona Lisa housed in the Louvre Museum?",
    "Is English the official language of the Netherlands?",
    "Is Elon Musk the CEO of Microsoft?",
    "Is the Pacific Ocean the largest ocean on Earth?",
    'Is "The Great Gatsby" written by F. Scott Fitzgerald?',
    'Is the Statue of Liberty located in London?'
]

for prompt in prompts:
    print("Question: %s" % prompt)
    completion = llm(prompt)
    print("Answer: %s \n" % completion)

    answer_yes_no_questions(prompt, completion)
    