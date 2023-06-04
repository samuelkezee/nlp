import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

file_path = 'C:\\Users\\User\\Desktop\\nlpp\\NLP.txt'
with open(file_path, 'r') as file:
    text = file.read()
tokens = word_tokenize(text)
word_freq = Counter(tokens)

for word, freq in word_freq.items():
    print(word, freq)



