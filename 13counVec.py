from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Example data
data = ['apple', 'banana', 'cherry', 'apple', 'orange']

# Initialize the OneHotEncoder
encoder = OneHotEncoder(sparse=False)

# Reshape the data to a 2D array
data_reshaped = [[value] for value in data]

# Fit and transform the data using OneHotEncoder
encoded_data = encoder.fit_transform(data_reshaped)

# Print the encoded data
print(encoded_data)
