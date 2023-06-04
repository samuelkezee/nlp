def standardize_text(text):
    # Custom lookup dictionary
    lookup_dict = {
        "u": "you",
        "ur": "your",
        "gr8": "great",
        "b4": "before",
        "2": "to",
        "r": "are",
        "pls": "please"
        # Add more mappings as needed
    }

    # Split text into individual words
    words = text.split()

    # Standardize words
    standardized_words = []
    for word in words:
        if word.lower() in lookup_dict:
            standardized_words.append(lookup_dict[word.lower()])
        else:
            standardized_words.append(word)

    # Join the standardized words back into a string
    standardized_text = ' '.join(standardized_words)

    return standardized_text


# Example usage
text = "u r gr8! b4 we go, pls confirm."
standardized_text = standardize_text(text)
print(standardized_text)
