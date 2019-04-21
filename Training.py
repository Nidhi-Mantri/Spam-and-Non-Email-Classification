from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC  
svclassifier = SVC(kernel='linear')
import os
import numpy as np

def main():
    print "*******************************************"
    # loading mat file
    # loading training data
    email1 = np.load("Ham.npy")
    email2 = np.load("Account_Locked.npy")
    os.chdir("D:\\Python5th\\AI\\Preprocess\\Test_Data")
    #a = np.load("Ham2.npy")
    #b = np.load("Spam4.npy")
    c = np.load("Ham6.npy")
    d = np.load("Spam6.npy")
    X_test = np.concatenate((c, d), axis = 0)
    
    test_a = np.zeros((1500, 1))
    test_b = np.ones((4500, 1))
    #print test_b
    y_test = np.concatenate((test_a, test_b), axis = 0)
    y_test = y_test.ravel()
    train_data = np.load("H2S4H4S3H5S1.npy")
    train_a = np.zeros((4361, 1))
    train_b = np.ones((4500, 1))
    train_c = np.zeros((1500, 1))
    train_d = np.ones((1500, 1))
    train_e = np.zeros((1500, 1))
    train_f = np.ones((1500, 1))
    train_m = np.concatenate((train_a, train_b), axis = 0)
    train_n = np.concatenate((train_m, train_c), axis = 0)
    train_o = np.concatenate((train_n, train_d), axis = 0)
    train_p = np.concatenate((train_o, train_e), axis = 0)
    train_y = np.concatenate((train_p, train_f), axis = 0)    
    #print train_y
    train_y = train_y.ravel()
    print "Please wait, it will take upto 10 minutes.........."
    # Training of the classifier
    svclassifier.fit(train_data, train_y)
    y_pred = svclassifier.predict(X_test)
    print "Confusion Matrix for this classifier is : -"
    print(confusion_matrix(y_test, y_pred))
    print "Classification Report for this classifier is :- "
    print(classification_report(y_test, y_pred))
    print "Accuracy Score is : - ", accuracy_score(y_test, y_pred)
    print "Result of your emails is : -"
    email = 0
    for i in [email1, email2]:
        print "Email", email+1, " -",
        result = svclassifier.predict(i)
        if result == 0:
            print "Ham Email"
        else:
            print "Spam Email"
        email += 1
    
if __name__ == "__main__":
    main()
