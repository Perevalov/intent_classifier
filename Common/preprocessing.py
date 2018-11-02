from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import FeatureHasher
from nltk.corpus import stopwords as sw
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
#from jamspell import TSpellCorrector
import pymorphy2
import re
import numpy as np
stopwords = sw.words('russian')
#jam = TSpellCorrector()
#jam.LoadLangModel('..//..//jamspell//jamspell_model.bin')
tokenizer = RegexpTokenizer(r'\w+')
morph = pymorphy2.MorphAnalyzer()
stemmer = RussianStemmer()

custom_stopwords = ['сколько','во-сколько','здравствовать','здрасте', 'вообще','это', 'ещё', 'значит', 'значить','этмый','либо','хотя','таки','кроме','просто','её','сей','оно','ничто','го', 'ой', 'сегодня', 'спасибо'
'январь','февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
def preprocess_word(word):
    return morph.parse(word)[0].normal_form.lower()

def read_to_list(filename):
    with open(filename, 'r',encoding='utf8') as f:
        content = f.readlines()
        content = [x.strip() for x in content] 
    return content

def preprocess_list(list_):
    new_list = []
    for l in list_:
        words = tokenizer.tokenize(l)
        
        new_words = [preprocess_word(word) for word in words 
                        if morph.parse(word)[0].normal_form not in stopwords #morph.parse(jam.FixFragment(word))[0].normal_form not in stopwords 
                        and not any(char.isdigit() for char in word)
                        and not bool(re.search(r'[a-zA-Z]', word))
                        and morph.parse(word)[0].normal_form.lower() not in custom_stopwords #morph.parse(jam.FixFragment(word))[0].normal_form.lower() not in custom_stopwords
                    ]
        new_list.append(' '.join(w for w in new_words))
    return new_list

def preprocess_eng_list(list_):
    new_list = []
    for l in list_:
        words = tokenizer.tokenize(l)
        
        new_words = [word for word in words 
                        if morph.parse(word)[0].normal_form not in stopwords #morph.parse(jam.FixFragment(word))[0].normal_form not in stopwords 
                        and not any(char.isdigit() for char in word)
                        and morph.parse(word)[0].normal_form.lower() not in custom_stopwords #morph.parse(jam.FixFragment(word))[0].normal_form.lower() not in custom_stopwords
                    ]
        new_list.append(' '.join(w for w in new_words))
    return new_list

def sentence2list(sentence):
    words = tokenizer.tokenize(sentence)
    words_ = []
    for w in words:
        words_.append(w+"_"+morph.parse(w)[0].tag.POS)

    return words_
