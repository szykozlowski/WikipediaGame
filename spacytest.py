import spacy 


nlp = spacy.load('en_core_web_lg') 

file_path = "words.txt"
with open(file_path, 'r') as file:
    words_list = file.read().split(',')


formatted_string = ""
for word in words_list:
    formatted_string += word

tokens = nlp(formatted_string) 


for i in range(0,len(tokens),2):

    token1, token2 = tokens[i], tokens[i + 1] 
  
    print(token1," ",token2," ", token1.similarity(token2)) 
    