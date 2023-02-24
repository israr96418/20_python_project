quiz_dic =  {
    'question1':{
        'question':'what is capital of Pakistan',
        'answer': 'Islamabad'
    },

    'question2': {
        'question': 'what is capital of India',
        'answer': 'Dehli'
    },

    'question3': {
        'question': 'what is capital of France',
        'answer': 'Paris'
    },

    'question4': {
        'question': 'what is capital of Italy',
        'answer': 'Rome'
    },

    'question5': {
        'question': 'what is capital of USA',
        'answer': 'WasingtonDc'
    },

    'question6': {
        'question': 'what is capital of Postugal',
        'answer': 'Lisbian'
    },

    'question7': {
        'question': 'what is capital of Austria',
        'answer': 'Vienna'
    },
}


# To show question to user and get input
#then we compare answer with correct one and show score to user

score = 0

for key , value in quiz_dic.items():
    print(value['question'])
    ans = input("Enter your answer: ")

    if ans.lower() == value['answer'].lower():
        print('Correct')
        score = score +1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Your answer is wrong")
        print("Your score is: ", str(score))
        print('Correct answer is: ' + value['answer'])
        print("")
        print("")

print('Your score is:' + str(score) + ' out of 7')
print("Percenatge: ", str(int(score/7 * 100)) + "%")

if score < 5:
    print('Sorry you are fail')