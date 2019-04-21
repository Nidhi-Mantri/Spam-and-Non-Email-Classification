import re
import os
import shutil
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
Lemmatizer = WordNetLemmatizer()
stop_words = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against",
              "all", "almost", "alone", "along", "already", "also","although","always","am","among",
              "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone",
              "anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became",
              "because","become","becomes", "becoming", "been", "before", "beforehand", "behind",
              "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but",
              "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe",
              "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven",
              "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
              "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first",
              "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further",
              "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
              "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
              "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep",
              "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile",
              "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must",
              "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no",
              "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often",
              "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours",
              "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re",
              "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should",
              "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
              "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten",
              "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby",
              "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though",
              "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards",
              "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well",
              "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas",
              "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who",
              "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would",
              "yet", "you", "your", "yours", "yourself", "yourselves"]

def preprocess(input_file, new_name):
    new_file = open(new_name, 'w')
    with open(input_file, "r") as sample_email:
        email = sample_email.readlines()
    email = ''.join(email)
    #print email
    #print "______"
    # Step 1 Lower case
    email = email.lower()
    #print email

    # Step 2 Strip all HTMLs
    email = re.sub('<[^<>]+>', ' ', email)

    # Step 3 Replace all numbers with string "number"
    email = re.sub('[\d]+', ' ', email)

    # Step 4 Handle URLs
    email = re.sub('(http|https) : / / [^\s]*', 'urls', email)

    # Step 5 Handle Email address
    email = re.sub('[^\s]+@[^\s]+', 'emailaddr', email)

    # Step 6 Handle dollar sign
    email = re.sub('[$]+', 'dollar', email)

    # Step 7 Remove all punctuation marks
    email = re.sub('[\@+|\/+|\#+|\.+|\-+|\:+|\&+|\*+|\++]', ' ', email)     # '@/#.-:&*+
    email = re.sub('[|\=+|\[+|\]+|\?+|\!+|\(+|\)+|\{+|\}+|\,+|]', ' ', email)        # '=[]?!(){},'
    email = re.sub('[\'+|\"+|\>+|\_+|\<+|\;+|\%+]', ' ', email)            # " ' ' " >_<;%
    email = re.sub("[^a-zA-Z]"," ", email)
    # Step 8 Remove all whitespaces(more than one) and \t, \n, ...
    email = re.sub('\ +|[\s]+', ' ', email)

    # Step 9 Lemmatizing of words from the email, not in stop_words
    #print email
    lematize_email = []
    #email = email.split(' ')
    email_tokens = word_tokenize(email)
    #print email_tokens
    for word in email_tokens:
        #print word
        if word not in stop_words:
            lematize_email.append(Lemmatizer.lemmatize(word))

    lematize_email = ' '.join(lematize_email)
    email = lematize_email
    new_file.write("%s" % email)
    new_file.close()
    #shutil.move("C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\Enron_1\\Spam\\"+new_name, "C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\Preprocess\\Spam1\\"+new_name)
    print input_file
    return email


def main():
    '''files = []
    for i in os.listdir("C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\Enron_1\\Spam\\"):
        files.append(i)
    #print files
    os.chdir("C:\\Users\\Nidhi\\Desktop\\Python5th\\AI\\Enron_1\\Spam\\")
    for i in files:
        new_name = 'p'+i
        preprocess(i, new_name)'''
    preprocess("Suspended_Account.txt", "pSuspended_Account.txt")

if __name__ == "__main__":
    main()
