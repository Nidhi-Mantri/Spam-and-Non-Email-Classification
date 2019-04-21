import ast
from collections import Counter

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = list(alphabet)
    with open("dictionary.txt", "r")as my_file:
        dictionary = ast.literal_eval(my_file.read())
    print len(dictionary.keys())
    for i in dictionary.keys():
        if i in alphabet:
            del dictionary[i]
    counts = Counter(dictionary)
    final_words = []
    for word, freq in counts.most_common(25000):
        final_words.append(word)
    file_w = open("final_words.txt", "w")
    file_w.write("%s" % final_words)
    file_w.close()
    #print dictionary
    #word_count_vector(dictionary)

if __name__ == "__main__":
    main()
