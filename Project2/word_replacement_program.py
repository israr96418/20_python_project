def word_replacement():
    str = 'Being a software enginner we must flexible with technology'
    word_to_replace = input("Enter word that you want to replace: ")
    word_replacement = input("Enter word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

word_replacement()
