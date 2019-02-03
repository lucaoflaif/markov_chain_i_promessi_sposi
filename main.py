import re
import pprint as pp
from utils import *

mod = input("(N)ew training/(E)xisting model: ")
if mod == 'N': model_name = input("model name): ")
predict_lenght = int(input("Num of sentences to generate: "))

if mod == 'N':
    file_name = input("file text name: ")
    m_chain = {}

    print("OPENING FILE")
    with open(file_name, "r") as text_file:
        print("FILE OPEN")
        text = text_file.read()
    print("FILE CLOSED")

    text = re.split('(\W)',text)
    text = [word for word in text if not (word.isspace() or word=='')]

    print("TEXT FORMATTED, BUILDING CHAIN...")
    build_chain(text, m_chain)
    save_obj(m_chain, model_name)
    print("SAVED")

elif mod == 'E': 
    model_name = "trained_markov_chain_on_i_promessi_sposi"
    m_chain = load_obj(model_name)

if __name__ == '__main__':
    word = input("First word: ")
    generated_text = [word,]

    count=0
    while (count <= predict_lenght):
        word = predict_next_word(word, m_chain)
        generated_text.append(word)

        if word == '.': count +=1

    print(format_string(generated_text))
