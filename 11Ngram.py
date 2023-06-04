import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

sentence = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(sentence)

N = 2
n_grams = list(ngrams(tokens, N))
for gram in n_grams:
    print(gram)
