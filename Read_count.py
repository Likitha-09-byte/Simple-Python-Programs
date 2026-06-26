#Read a file and count the word frequency 

def count_word_frequency(file_path):
  #Empty dictionary
  word_count={}
  #Open the file in read mode
  with open(file_path,'r')as file:
    #Using for loop spliting the line into words
    for line in file:
      words = line.split()
      #Looping over the words 
      for words in word:
        word = word.lower().strip('.,!?;:"\'')
        #Calculate the word count
        word_count[word]= word_count.get(word,0)+1
  return word_count
filepath ='words.txt'

word_frequency = count_word_frequency(filepath)
print(word_frequency)