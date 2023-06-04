'''import io
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words=set(stopwords.words('english'))
file=open("C:\\Users\\User\\Desktop\\nlpp\\NLP.txt")
line=file.read()
words=file.split()
for i in words:
    if not i in stop_words:
        appendFile=open('C:\\Users\\User\\Desktop\\nlpp\\NLP.txt','a')
        appendFile.write(" "+i)
        appendFile.close()'''
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
with open("C:\\Users\\User\\Desktop\\nlpp\\NLP.txt",'r') as file:
    text=file.read()

tokens = word_tokenize(text)
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
for token in filtered_tokens:
    print(token)
