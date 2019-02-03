from numpy.random import choice
from collections import Counter
from string import punctuation
import pickle

def build_chain(text, m_chain):
    for word in text:
        if not word in m_chain:
            m_chain[word] = words_associated_with_word(word, text)

def words_associated_with_word(word, text):
    """Example: 
       text: ['I', 'ate', 'an', 'apple', 'then', 'I', 'had', 'a', 'shower']
       word: I
       return: ['ate', 'had']
    """
    words = []
    for idx in range(len(text)-1):
        if text[idx] == word: words.append(text[idx+1])
    return words

def count_elements(elements_dict):
    return dict(Counter(elements_dict))

def normalize(vector):
    sum_vect = sum(vector)
    return [float(value)/sum_vect for value in vector]

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def format_string(split_string):
    punc = set(punctuation)
    return ''.join(w if set(w) <= punc else ' '+w for w in split_string).lstrip()

def predict_next_word(word, m_chain):
    elements_dict = count_elements(m_chain[word])
    values = list(elements_dict.keys())

    if len(values) > 1:
        weights = normalize(list(elements_dict.values()))
        word = choice(values, 1, p=weights)[0]
    else:
        word = values[0]
    return word