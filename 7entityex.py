import

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Example text
text = "Apple Inc. is planning to open a new store in New York City."

# Process the text
doc = nlp(text)

# Extract entities
entities = [(entity.text, entity.label_) for entity in doc.ents]

# Print the extracted entities
for entity, label in entities:
    print(entity, label)
