##CS 101
##Program 6
##Spring 2018
##
##Christian Rodas
##cmrnmc@mail.umkc.edu
##
##PROGRAM: Taking in text and finding the synoyms most closely accosiated with a word
##  The program will take in a file full text, then it will go through that text 
##  and try to find a synoym for that from a dictionary. 
##    
##ALGORITHM:
##    1. Import Modules csv, math, re
##    2. Create functions for program
##    3. Begin program by opening the first file
##    4. First function is called to standardize and organize text
##    5  Second function is called to begin building synoms from the first function
##    6  Third function is called to start looking up the closest synonyms from second funtion##    7 Clears screen when button is pressed
##    8  Run similartiy test to find best words
##
##Error Handling: Program freezes if too much text is read at once.
##
##Other Comments: 
##
##################################################################################

# Part 1
import csv
import math
import re

# Part 2
def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''
    
    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    
    return dot_product / (norm(vec1) * norm(vec2))



def get_sentence_lists(text):
    ''' Returns all sentences from the text into a list'''

# Lowercases all characters
    text = str.lower(text)

#removing punctuation
    text = text.replace(":","")
    text = text.replace(";","")
    text = text.replace("--","")
    text = text.replace("'","")
    text = text.replace('"',"")
    text = text.replace("(","")
    text = text.replace(")","")

# Seperates text into words
    text= text.split()

    words_list = text


# Compiles all of the sentences from the file
    sentence_list = []
    temp_sentence_list = []
    for words in words_list:
        
        temp_sentence_list.append(words)

# Checks if it is the last word in the sentences and starts a list for a new sentence
        if words[-1] == "!" or words[-1] == "." or words[-1] == "?":

            temp_sentence_list.append(words)
            
            sentence_list.append(temp_sentence_list)

            temp_sentence_list = []

    return sentence_list


def get_sentence_lists_from_files(files : list):
    ''' Keeps track of the files and thier sentences'''

    master_file = files
        
    return master_file


def build_semantic_descriptors(sentences: list):
    ''' Sets a key for all individual words and adds all words from that same
        sentence as value, couting repititive accossiated words'''
    
    dict_of_words = {}

    for sentence in sentences:
 
        for word in sentence:

            try:
                if not word in dict_of_words:
                    next_word = sentence[sentence.index(word)+1]
 
                    dict_of_words[word]={}
                    dict_of_words[word][next_word] = 1
                else:
                    next_word = sentence[sentence.index(word)+1]

                    for key in dict_of_words.values():

                        for key2 in key.items():
 
                            if next_word in key:
                                key[next_word] += 1
                            elif not next_word in key:
                                    key[next_word] = 1
    
# Catches errors and keeps program going           
            except IndexError:
                pass
            
            except RuntimeError:
                pass

                
    return dict_of_words
    

    
def most_similar_word(word, choices, semantic_descriptors):
    ''' Gets a user word, and finds the most accossiated values with that word'''

    if word in choices:
        print("word found")
        print(semantic_descriptors.get(word))

    else:
        print("word not an option")
    
    pass


def run_similarity_test(filename, semantic_descriptors):
    ''' Shows which word the most accossiated words'''
    pass




# Part 3 Begins program
if __name__ == "__main__":

# Which files are available to be opened
    files = ["AdventuresOfTomSawyer.txt", "AliceInWonderland.txt",
             "TaleOfTwoCities.txt", "warandpeace.txt", "GreatExpectations.txt"]

# Opens file
    filename = str(input("Enter a file name to open:"))
    if filename in files:
        print("file found")
    else:
        print("File not found")
    
    fh = open(filename)
    
###Program freezes if too much is read at once
    contents = fh.read(1000)


#Part 4 First function is called to standardize and organize text
    step_1 = get_sentence_lists(contents)


#Part 5 Second function is called to begin building synoms from the first function
    step_2 = build_semantic_descriptors(step_1)
          
#Part 6 Third function is called to start looking up the closest synonyms from second funtion
    word = str(input("What word to look up?:"))
    choices = step_2
    semantic_descriptors = step_2

    step_3 = most_similar_word(word, choices, semantic_descriptors)
    print(step_3)

# Part 7 Run similartiy test to find best words
    step_4 = run_similarity_test(filename, semantic_descriptors)

    
    

    

    


           





    
