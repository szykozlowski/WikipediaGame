import spacy 


nlp = spacy.load('en_core_web_lg') 


word_test = "Exponentation"

word_list = "Power"


word_test = nlp(word_test)

word_list = nlp(word_list)


print("Similarity:", word_list.similarity(word_test)) 


'''
print("Enter two space-separated words") 
words = input() 
  
tokens = nlp(words)

for token in tokens: 

    print(token.text, token.has_vector, token.vector_norm, token.is_oov) 
  
token1, token2 = tokens[0], tokens[1] 
  
print("Similarity:", token1.similarity(token2)) 


'''