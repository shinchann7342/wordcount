import os
import pathlib
import matplotlib.pyplot as plt #for plotting as graph
def main(): 
    #enter your script in script.txt file before rnning the application
    text = open("script.txt", "r",errors='ignore') #if you cant correct the error ignore it
    file2=open("data.txt","w+")
    wordx = []
    count = []
    d = dict()
    
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
       
        for word in words:
            if word in d:
                 d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()):
        #print(key, ":", d[key])
        #my_list = []
        #my_list.append([key,d[key]])
        #print(my_list)
        alphanumeric=" "
        for character in key:
            if character.isalnum():
                alphanumeric += character
        
        file2.write(alphanumeric)
        file2.write(":")
        file2.write(str(d[key]))
        file2.write("\n")
        #myfun(key, d[key])
    f = open('data.txt','r')
    for row in f:
        row = row.split(":")
        wordx.append(row[0])
        count.append(int(row[1]))

    plt.barh(wordx,count , color = 'g', label = 'File Data')

    plt.ylabel('words', fontsize = 6)
    plt.xlabel('number of times observed', fontsize = 6)

    plt.title('Word Count', fontsize = 20)
    plt.legend()
    plt.show()
    #for key in list(d.keys()):
    
        
    #myfun('the','end')
main()



