import math

def CalcScore(sentiment):#get the average score
    count = len(sentiment)
    i = 0
    avg = 0
    avgCount = 0
    while i < count:
        mag = sentiment[i][1]
        if mag < 1.45: mag = 1
        elif mag < 2.45: mag = 2
        elif mag < 3.45: mag = 3
        elif mag < 4.45: mag = 4
        else: mag = 5
        print(mag)
        avg += sentiment[i][0]*mag
        avgCount += mag
        i += 1
    avg = avg/avgCount

    return avg

def UserScore(user, value):
    if user == "Netflix":
        score = math.ceil(100*(value+1)/2)
    elif user == "Consumer":
        score = math.ceil(2+4*(value+1))/2
    return score

