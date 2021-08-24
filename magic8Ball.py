import random
def getCorrectNumber(answerNum):
    if answerNum == 0:
        return "Are u kidding me!!"
    elif answerNum == 1:
        return "May be u are correct"
    elif answerNum == 2:
        return "It is certain"
    elif answerNum == 3:
        return "Yesss"
    elif answerNum == 4:
        return "No chance"
    elif answerNum == 5:
        return "Kihooo..no its not"
    elif answerNum == 6:
        return "dum dum dumb you are!!"
    elif answerNum == 7:
        return "Go home and sleep well"
    elif answerNum == 8:
        return "Bad luck buddy!!"
    elif answerNum == 9:
        return "Try Again!!"

print(getCorrectNumber(random.randint(1,9)))
