# programe 1 for dictionary

# exits = True
#
# def word_dic():
#     global exits
#     dict_for_word ={
#         'hi':"sanga chal de",
#         'apple': 'Type of fruit',
#         'mobile': "is a device used for calling, internet, social media"
#     }
#
#     while exits == True:
#         word = input("Enter your word: ")
#
#         if word.lower() in dict_for_word:
#             print("word meaning: ", dict_for_word[word])
#         else:
#             print('word are not present in my dictionary')
#             # global exit
#             exits = False
#
#
# if __name__ == '__main__':
#     word_dic()


########################################################################
# programe 2 for dictionary by using python library(PythonDictionary)

# from PyDictionary import PyDictionary


#PyDictionary give us not only the meaning of the words but also give use synonmy, antonmy,
# we can also get meaning of word in differen language-->Translate

# we can use PyDictionay in 2 ways
#1: we can create an instance/object of python and pass words as an argument and get meaning
#2: we passed list of words as an arguments to the instaance/object


#create an instance of PyDictionary()
# dictionary = PyDictionary()


# print(dictionary.meaning('life'))
# print(dictionary.synonym('life'))
# print(dictionary.antonym('life'))
# print(dictionary.translate('life', 'ur'))   #it will give meaning of word in urdu(ur),hindi(hi), spanish(es)

##########################################################################

# programe 2 for dictionary by using python library(PythonDictionary)

from PyDictionary import PyDictionary

dictionary = PyDictionary("hotel","ambush","nonchalant","perceptive")


'''This print the meanings of all the words'''
print(dictionary.printMeanings())

'''This will return meanings as dictionaries'''
print(dictionary.getMeanings())

print (dictionary.getSynonyms())
'''This will translate all words to Hindi'''
print (dictionary.translateTo("hi"))

