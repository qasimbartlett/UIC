def Positive(word):
    if word in open('PositiveWords.txt').read().split():
        return True
    else:
        return False
#Opening the positive words text file and splitting the words

def Negative(word):
    if word in open('text negative.txt').read().split():
        return True
    else:
        return False
#Opening the negative words text file and splitting the words
    


num_positive_word=0
num_negative_word=0
num_Neutral_word=0
#Defining the counts

with open('book.txt','r') as f:      #Opening the book
    for line in f:
        for word in line.split():
            
            if Positive(word):
               num_positive_word+=1
            elif Negative(word):
               num_negative_word+=1
            else:
               num_Neutral_word+=1
#Telling the program that when reading the book if it finds a positive word add 1 to the count and same with the negative/neutral words



print (' there are this many positive words',num_positive_word)
print (' there are this many negative words',num_negative_word)
print ('there are this many neutral words',num_Neutral_word)

# Finally it ends up printing how many positive, negative, and neutral words there are
