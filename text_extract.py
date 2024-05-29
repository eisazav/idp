import fitz

from sklearn.feature_extraction.text import TfidfVectorizer

from model_train import X_train

from re import sub
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import unicodedata
nltk.download('stopwords')
nltk.download('punkt')

stop_words_sp = stopwords.words('spanish')
stemmer = SnowballStemmer('spanish')

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def clean_text(text):
    words = []
    subwords = word_tokenize(text, language="spanish")
    for item in subwords:
        item = item.lower()
        item = sub("[^a-záéíóúñü]", "", item)
        if not item in stop_words_sp and len(item) > 3:
            item = strip_accents(item)
            item = stemmer.stem(item)
            words.append(item)
    return words

tfidf_vectorizador = TfidfVectorizer(tokenizer = clean_text)
tfidf_vectorizador.fit_transform(X_train)

def vectorize_text(text):
    return tfidf_vectorizador.transform([text])

def get_raw_content(file):
    text = ""
    with fitz.open("pdf", file) as doc:
        for page in doc:
            text += page.get_text()
    return text
  