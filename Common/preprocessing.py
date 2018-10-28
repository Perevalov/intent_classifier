from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import FeatureHasher
from nltk.corpus import stopwords as sw
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
from jamspell import TSpellCorrector
import pymorphy2
import re
import numpy as np
from sklearn.cluster import KMeans
stopwords = sw.words('russian')
jam = TSpellCorrector()
jam.LoadLangModel('..//..//jamspell//jamspell_model.bin')
tokenizer = RegexpTokenizer(r'\w+')
morph = pymorphy2.MorphAnalyzer()
stemmer = RussianStemmer()

custom_stopwords = ['сколько','во-сколько','здравствовать','здрасте']
def preprocess_word(word):
    return morph.parse(jam.FixFragment(word))[0].normal_form.lower()

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
                        if morph.parse(jam.FixFragment(word))[0].normal_form not in stopwords 
                        and not any(char.isdigit() for char in word)
                        and not bool(re.search(r'[a-zA-Z]', word))
                        and morph.parse(jam.FixFragment(word))[0].normal_form.lower() not in custom_stopwords
                    ]
        new_list.append(' '.join(w for w in new_words))
    return new_list
