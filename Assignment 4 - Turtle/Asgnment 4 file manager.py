import turtle
import csv

user_file = input('Enter file to open and draw:')

pythonlogo = []

try:
    f = open(user_file)

    lines = f.readlines()

    print(lines)
    print()


    string_lines = str(lines)
    my_tokens = string_lines.split(',')
    print(my_tokens)
    print()
    
    print(my_tokens[10])
    print()

    my_tokens = str(my_tokens)
    my_tokens2 = my_tokens.split('\\n')
    print(my_tokens2)
    print()
    
    print(my_tokens2[0][0])



    

    f.close()

except FileNotFoundError:
    print('Could not open file :', user_file)
