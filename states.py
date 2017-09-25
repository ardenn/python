#!/usr/bin/python3
# randomQuiz -create 35 quizzes and answers in random order.

import random
# quiz data of states and their capitals
stateCapitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

letters = ["A", "B", "C", "D"]
# create list of states and list of capitals
states = [state for state in stateCapitals.keys()]

# generate 10 question files
for q in range(1, 3):
    answerList = []
    with open("student%d" % q, "w") as studentFile:
        studentFile.write("Date:............\n")
        studentFile.write("Name:......................\n\n")

        random.shuffle(states)
        quizCount = 1
        for state in states:
            capitals = [cap for cap in stateCapitals.values()]
            studentFile.write(
                "{}. The capital city of {} is:\n".format(
                    quizCount, state))

            correctAnswer = stateCapitals[state]
            capitals.remove(correctAnswer)
            wrongAnswers = random.sample(capitals, 3)
            choices = wrongAnswers + [correctAnswer]
            random.shuffle(choices)
            answerList.append(letters[choices.index(correctAnswer)])
            quizCount += 1

            for letter, choice in zip(letters, choices):
                studentFile.write("\t{} {}\n".format(letter, choice))

    with open("answer%d" % q, "w") as answerFile:
        answerFile.write("Date:..............\n")
        answerFile.write("Name:.......................\n\n")

        answerCount = 1
        for answer in answerList:
            answerFile.write("{}. {}\n".format(answerCount, answer))
            answerCount += 1
