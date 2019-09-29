import math

def CalcScore(sentiment):  # Calculates the average score of the sentiment
    count = len(sentiment)  # Number of seniment/magnitude pairs in the passed-in array
    i = 0
    avg = 0
    avgCount = 0
    # Include the sentiment in the average multiple times depending on magnitude
    while i < count:
        mag = sentiment[i][1]  # Extract magnitude from the array for the current record
        if mag < 0.40 : mag = 1  # Magnitude ranges from 0 to infinity, though most are less than 1
        elif mag < 0.6 : mag = 2
        elif mag < 0.8 : mag = 3
        elif mag < 1 : mag = 4
        else: mag = 5

        avg += sentiment[i][0]*mag  # Add the current sentiment to the accumulating variable [magnitude] number of times
        avgCount += mag  # Add the [magnitude number of times] to the average divisor
        i += 1
    avg = avg/avgCount  # Calculate the sentiment average
    return avg

def UserScore(user, value):  # Design two different marking system for different users.
    if user == "Netflix":
        score = math.ceil(100*((value+1)/2))  # Return integer value from 1-100
    elif user == "Consumer":
        num = math.floor((((value+1)/2)*40)+10)  # Return value from 1-5 stars in half-star increments
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
