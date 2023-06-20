word = str(input("Enter your Word\n"))
word = word.lower()
unique_word = set(word)
if len(word) == len(unique_word):
	print("its isogram")
else:
	print("its not isogram")

