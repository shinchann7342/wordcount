import os
import pathlib
import matplotlib.pyplot as plt #for plotting as graph
def main(): 
    #enter your script in script.txt file before rnning the application
    text = open("script.txt", "r",errors='ignore') #if you cant correct the error ignore it
    file2=open("data.txt","w+") #ocreates a new text files and stores the words and its count for plotting
    wordx = [] #lists wordx and count for plotting the bar graph
    count = []
    d = dict() #dictionary for reading and processing script.txt
    
    for line in text: #loop for traversing script.txt and splitting the words
        line = line.strip() #returns a copy of the string by removing both the leading and the trailing characters
        line = line.lower() #converts to lower case to avoid repeation of similar words
        words = line.split(" ") #splits when a space is observed
       
        for word in words: #loop for storing the word temproarily in the dictonary
            if word in d:
                 d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()): #loop for removing any special characters 
        alphanumeric=" "
        for character in key:
            if character.isalnum():
                alphanumeric += character
        
        file2.write(alphanumeric) #writes the word in the new file created
        file2.write(":") 
        file2.write(str(d[key])) #writes the count of the respective word
        file2.write("\n")
    f = open('data.txt','r') 
    for row in f: #loop for getting the words and count from the new text file and splits it as two rows
        row = row.split(":") #splits when a semicolon is observed
        wordx.append(row[0]) #appends the data to the lists previously created
        count.append(int(row[1]))

    plt.barh(wordx,count , color = 'g', label = 'File Data') #plots an horizontal bargraph for the the respective x and y axes

    plt.ylabel('words', fontsize = 6) #as it says font size lol
    plt.xlabel('number of times observed', fontsize = 6)

    plt.title('Word Count', fontsize = 20) #title of the bar graph
    plt.legend() #to reflect data displayed in the graph such as x and ya axes color etc
    plt.savefig('fig1.png') #saves the graph as a png (image) file
    plt.show() #shows the graph 
     
    
main()



