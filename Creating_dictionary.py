from nltk import word_tokenize
import os
import shutil
import ast

def create_word_dictionary(emailFile, dictionary):
    with open(emailFile, 'r') as email_file:
        email = email_file.readlines()
    email = ''.join(email)
    
    email = word_tokenize(email)
    for word in email:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    print emailFile
    return dictionary

def main():
    directory = "C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\Preprocess\\"
    folders = []
    dictionary = {}
    for folder in os.listdir(directory):
        if folder != 'Test_Data':
            print folder+"------------------>"
            folders.append(folder)
            os.chdir(directory+folder+"\\")
            for i in os.listdir(directory+folder+"\\"):
                dictionary = create_word_dictionary(i, dictionary)
    print folders
    os.chdir("C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\")
    dict_file = open("dictionary.txt", "w")
    dict_file.write("%s"% dictionary)
    dict_file.close()
    '''
    with open("dictionary.txt", "r")as my_file:
        dictionary = ast.literal_eval(my_file.read())
    print dictionary
    '''
    
if __name__ == "__main__":
    main()
