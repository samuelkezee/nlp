import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('wordnet')

# Example text
text = "I am running in the park and saw a runner running."

# Tokenize the text
tokens = word_tokenize(text)

# Perform stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(token) for token in tokens]

# Perform lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]

# Print the stemmed and lemmatized words
print("Stemmed words:", stemmed_words)
print("Lemmatized words:", lemmatized_words)
