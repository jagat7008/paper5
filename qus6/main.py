import re
with open('text.txt', 'r') as f:
    lines = f.readlines()
total = 0 
for line in lines:
    integers = re.findall(r'\d+', line)  # Extract all integers as a list of strings
    integers = [int(i) for i in integers]  # Convert the list of strings to a list of integers
    concatenated_integers = int(''.join(map(str, integers)))  # Concatenate all integers in the line
    total += concatenated_integers  # Add the concatenated integers to the running total

print(total)  # Print the total sum of all integers in the file