word=input("Introduce una palabra: ")
word_len=len(word)
for n in range(word_len-1,-1,-1):
    print(word[n])