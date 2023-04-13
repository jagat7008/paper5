# import string

# sentence = "IneedtoworkveryhardtolearnmoreaboutalgorithmsinPython!"
# sentence = sentence.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
# words = sentence.split()
# total_length = sum(len(word) for word in words)
# average_length = total_length / len(words)
# print(average_length)


sentence = "I need to work very hard to learn more about algorithms in Python!"
l = len(sentence)
char = 0
for i in sentence:
    if i.isalpha():
        char += 1
print(l)
print(char)
result = char / l *100
print(result)







