#Program 6

import csv
import math
import random

sentence = []
i = 0
def sentences(input_sentence):
    i = i+1
    sentence = sentence+i
    print(sentence)

sentences('hello there')
sentences('hi there')
s


    print(contents)
    print('space')

    sentences = [s.strip() for s in re.split('[\.\?!]' , contents) if s]
    print(sentences)
    print()
    master_list.append(sentences)
    print(master_list)


    sentences = [s.strip() for s in re.split('[\.\?\!]' , contents) if s]
    print(sentences)
    print()

    print('splitting')
    print(len(sentences))

    for sentence in sentences:
        sentence = [sentence]
        print(sentence)
        master_list.append(sentence)

    print(master_list)
    print("^^^^^^^^^^^^^^^^^^^")


    contents = contents.split()



    word_dict= {}
    print(word_dict)
    test = [['test jack'],['test jack it going']]
    for sent in test:
        print(sent)
        
        for word in sent:
            print(word)
            try:
                if not word in word_dict:
                    next_word = sent[sent.index(word)+1]
                    word_dict[word]={}
                    word_dict[word][next_word] = 1
                else:
                    next_word = sent[send.index(word)+1]
                    print(next_word)
                    for key in word_dict.values():
                        print(key)
                        for key2 in key.items():
                            print(key2)
                            print(type(key2))
                            if next_word in key:
                                key[next_word]+=1
                            elif not next_word in key:
                                key[next_word] = 1
            except IndexError:
                pass
            
    print(word_dict)


        
    def __str__ (self):
        return (" %s this %d is %f " % (self.item_name, self.item_price, self.item_quantity))
        



                else:
                    next_word = sentence[sentence.index(word)+1]
                    print("else:next_word", next_word)
                    for key in word_dict.values():
                        print(key)
                        for key2 in key.items():
                            print(key2)
                            print(type(key2))
                            if next_word in key:
                                key[next_word] += 1
                            elif not next_word in key:
                                    key[next_word] = 1







    print('^^^^^^^^^^^^^^splitting')
    print(len(sentences))

    for sentence in sentences:
        sentence = [sentence]
        print(sentence)
        master_list.append(sentence)



    for words in text:
        print(words[-1])
        new_list = []
        new_list.append(words)
        if words[-1] == "!" or words[-1] == "." or words[-1] == "?":
            words = [words]
            print(words)
            print("^^^^^^^^")
    
        if words[-1] != "!" or words[-1] != "." or words[-1] != "?":



    words_list = text
    print(words_list)


    sentence_list = []
    for words in words_list:

        if words[-1] != "!" or words[-1] != "." or words[-1] != "?":
            print("not an ender word")
            sentence_list.append(words)
        
        if words[-1] == "!" or words[-1] == "." or words[-1] == "?":

            words = [words]
            print(words)
            print("^^^^^^^^")
        print(words)
    print(type(words))


        



            
    print(sentence_list)
    print(words_list[-5])




        
           """ temp_sentence_list.append(words)
            i = i +1
            print(temp_sentence_list)
            if words[-1] == "!" or words[-1] == "." or words[-1] == "?":
                i = i +1

                print(words)
                #remove peroid
                print("^^^^^^^^")
                temp_sentence_list.append(words)
                sentence_list = sentence_list + temp_sentence_list
                temp_sentence_list = []
                break"""














