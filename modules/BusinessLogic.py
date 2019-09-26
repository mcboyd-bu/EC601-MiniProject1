import math

def CalcScore(sentiment):#get the average score of the sentiment
    #get the parameters of the input
    count = len(sentiment)
    i = 0
    avg = 0
    avgCount = 0
    #change the values of the magnitude to a constant, according to different levels
    while i < count:
        mag = sentiment[i][1]
        if mag < 0.40 : mag = 1
        elif mag < 0.6 : mag = 2
        elif mag < 0.8 : mag = 3
        elif mag < 1 : mag = 4
        else: mag = 5

        avg += sentiment[i][0]*mag
        avgCount += mag
        i += 1
    avg = avg/avgCount

    return avg

def UserScore(user, value):#design two different marking system for different users.
    if user == "Netflix":
        score = math.ceil(100*((value+1)/2))
    elif user == "Consumer":
        num = math.floor((((value+1)/2)*40)+10)
        tens = num//10
        remainder = num-(tens*10)
        fives = 5*(remainder//5)
        if fives == 0:
            half = ""
        else:
            half = "." + str(fives)
        stars = str(tens) + half + " STARS"
        score = stars
    return score
