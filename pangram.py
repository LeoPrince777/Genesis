#M-1
Word_senten = str(input("Enter Your word_Sentence"))
x = len(set("abcdefghijklmnopqrstuvwxyz"))
y = len(set(Word_senten.lower()))
print(x)
print(y)
if x-y ==0:
	print("Given word is pangram")
else:
	print("Given word is not pangram")
#M-1
def pangram(word):
    x = len(set("abcdefghijklmnopqrstuvwxyz"))
    y = len(set(word.lower()))
    if x-y == 0:
    	return True
    return False
string = str(input("Enter your Word_Sentence"))
if pangram(string):
    print("Its PANGRAM")
else:
    print("Its not PANGRAM")    
              
