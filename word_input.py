from nltk import word_tokenize
import numpy.matlib as np
import os
import shutil
import sys

sys.stdout.flush()
def word_count_vector(dictionary):
    file_no = 0
    feature_matrix = np.zeros((1, 5000))
    with open("Ham.txt", 'r') as email_file:
        email = email_file.readlines()
    email = ''.join(email)
    email = word_tokenize(email)
    for word in email:
        if word in dictionary:
            #print 'True'
            index = dictionary.index(word)
            #print email.count(word)
            feature_matrix[file_no, index] = email.count(word)
        #sys.exit()
    file_no += 1
    np.save('Ham.npy', feature_matrix)
        
def main():
    with open("final_words.txt", "r") as words:
        final_words = words.readlines()
    final_words = ''.join(final_words)
    final_words = final_words.replace("['", '')
    final_words = final_words.replace("']", '')
    final_words = (final_words).split("', '")
    final_words = final_words[:5000]
    #print final_words[4999]
    word_count_vector(final_words)

if __name__ == "__main__":
    main()
