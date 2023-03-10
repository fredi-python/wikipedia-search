import wikipedia #pip install wikipedia

input_wiki = input('Wikipedia Search \n')
a = wikipedia.summary(input_wiki)
print(a) # print the result
