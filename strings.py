#Strings
sentence = "The quick brown fox jumped over the lazy dog"
#Builtin functionality
#functions
print(sentence)
print(sentence.upper()) #call a funtion
print(sentence.lower())
print(sentence.title())
print(sentence.count("dog"))
print(sentence.isspace())

sentence = "  "
if sentence.isspace() or sentence.isdigit() or sentence.isnumeric():
    print("Invalid Name")
else:
    print("Valid Name")