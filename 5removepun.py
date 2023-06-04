import nltk
import string
from nltk.tokenize import word_tokenize
nltk.download('punkt')

file_path = 'C:\\Users\\User\\Desktop\\nlpp\\NLP.txt'
with open(file_path, 'r') as file:
    text = file.read()
tokens = word_tokenize(text)


table = str.maketrans('', '', string.punctuation)
filtered_tokens = [token.translate(table) for token in tokens if token.translate(table)]

# Print the filtered tokens
for token in filtered_tokens:
    print(token)
