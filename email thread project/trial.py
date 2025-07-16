import nltk
nltk.download("average_perceptron_tagger")
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.data import find
print(find("tagger/averaged_perceptron_tagger/"))
text= "NLTK is a leading platform for building python programs to work with human language data. It\
    provides easy-to-use interface to over 50 corpora and lexical resources such as WordNet, alond with a\
    suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic\
    reasoning, wrapper for industrial-strength NLP libraries, and an active discussion forum."
tokens=word_tokenize(text)
tag=pos_tag(tokens)
print(tag)