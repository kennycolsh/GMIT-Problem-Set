#Solution for problem 6
#Ref Solution 1
#user_input  = input("Please enter a string of words : ")
#result = user_input.split(' ')[::2]
#print(result)
#https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
sentenceInput=(input ("Please enter sentence: "))

def splitstr(sentence):

    # Splitting sentence 
    sentenceList = sentence.split(" ")[::2]

    # see if only one word is entered
    if len(sentenceList) == 1:
        print("Entered sentence does not contain two words.")

  
    return sentenceList
#call function to test if string has one word
#adn split the sentence
print(splitstr(sentenceInput))