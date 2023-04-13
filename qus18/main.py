import pickle

# Define the dictionary
dct = {111: "Eric", 112: "Kyle", 113: "Butters"}

# Serialize the dictionary and write it to a file
with open('vicky.txt', 'wb') as file:
    pickle.dump(dct, file)

# Deserialize the data from the file into a new dictionary
with open('vicky.txt', 'rb') as file:
    dct2 = pickle.load(file)

# Access the value of the required key from the deserialized dictionary
print(dct2[112])  # Output: Kyle