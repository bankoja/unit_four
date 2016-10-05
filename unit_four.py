# James Bankole Unit 4 10/4/16

# Imported random because it is necessary in order to get random numbers.
import random

# Intro to the program.
print("Hello, welcome to the math facts game.")


def getProblemType():
    '''This function prompts the user to input the type of problem they want to solve.'''
    problemT = input("Please select what type of math problem you want to attempt. (+,- or x)")
    return problemT


def getMaxNumber():
    '''This function prompts the user for the max number that they would like for the problem.'''
    maxN = input("Please input the max number that you would like for this game.")
    return int(maxN)


def randomNumber(maxNumber):
    '''This is the function to retrieve the random number (it is run twice to get two random numbers).'''
    randomNOne = random.randint(0, maxNumber)
    return randomNOne


def problem(randomOne, randomTwo, problemType):
    '''This is the function that generates the problem and displays it to the user.'''
    problem = str(randomOne) + problemType + str(randomTwo)
    print("Your problem is", problem)


def answer():
    '''This is the function that prompts the user to input their guess to the problem.'''
    return int(input("What is the answer?"))


def problemTS(problemType, randomOne, randomTwo):
    '''This is the function that takes the problem type that the user inputted and solves the problem generated.'''
    if problemType == "-":
        return randomOne - randomTwo
    elif problemType == "x":
        return randomOne * randomTwo
    else:
        return randomOne + randomTwo


def final(userAnswer, correctAnswer):
    '''This function checks to see if the user's guess is correct by comparing it to the correct answer and then tells
theuser if they were right or not.'''
    if userAnswer == correctAnswer:
        return print("Congratulations, you are correct!")
    else:
        return print("I'm sorry, that is incorrect.")


def main():
    problemType = getProblemType()
    maxNumber = getMaxNumber()
    randomOne = randomNumber(maxNumber)
    randomTwo = randomNumber(maxNumber)
    problem(randomOne, randomTwo, problemType)
    problemTS(problemType, randomOne, randomTwo)
    userAnswer = answer()
    correctAnswer = problemTS(problemType, randomOne, randomTwo)
    final(userAnswer, correctAnswer)

main()
