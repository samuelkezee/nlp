
import nltk
from nltk import word_tokenize
file_path ='C:\\Users\\user\\Desktop\\nlp.txt'
with open(file_path, 'r') as file:
    contents = file.read()
    tokens=word_tokenize(contents)
for token in tokens:
    print(token)



