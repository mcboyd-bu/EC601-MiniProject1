import math

def CalcScore(sentiment, magnitude):#get the average score
    count = len(sentiment)
    i = 0
    avg = 0
    while i < count:
        avg += sentiment[i]*magnitude[i]
        i += 1
    avg = avg/count

    return avg

def UserScore(user, value):
    if user == "Netflix":
        score = math.ceil(100*(value+1)/2)
    elif user == "Consumer":
        score = math.ceil(2+4*(value+1))/2
    return score

