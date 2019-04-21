import os
import shutil
def processing(input_file, new_file):
    new_file = open(new_name, 'w')
    with open(input_file, "r") as file_i:        
        x = file_i.readline()
        while x:
            flag = 0
            if ("Subject:" in x) or ("subject :" in x) :    #or ("Subject :" in x) or ("subject :" in x)
                #print "S"
                line = file_i.readline()
                while line and "forwarded" not in line and "cc :" not in line and "to :" not in line and "from :" not in line:
                    #print line
                    new_file.write("%s\n"%line)
                    line = file_i.readline()
                #print "________________"
            x = line
            if ("forwarded" in x) or ("cc :" in x) or ("from :" in x) or ("to :" in x):
                line = file_i.readline()
                while line and "subject :" not in line:           #or "Subject :" not in line
                    line = file_i.readline()
                    flag = 1
            if flag == 0:
                x = file_i.readline()
                #print flag, x
            else:
                x = line
                #print flag, x
    print input_file
    new_file.close()
    shutil.move("D:\\enron6\\ham\\"+new_name, "D:\\Python5th\\AI\\Enron_6\\Ham\\"+new_name)
                
def main():
    files = []
    for i in os.listdir("D:\\enron6\\ham"):
        files.append(i)
    #print files
    os.chdir("D:\\enron6\\ham")
    for i in files:
        new_name = 'h_'+i
        processing(i, new_name)

if __name__ == "__main__":
    main()
