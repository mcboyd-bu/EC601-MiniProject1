import GoogleNatLangAPI as GNL
import BusinessLogic as BL
import Progress as PR
import time
from twitter_api import Get_twitter

try:  # Code to allow cross-compatible input for both Python 2.x and 3.x; from http://python3porting.com/differences.html?highlight=input
    input = raw_input
except NameError:
    pass

# Variables #
userType = ""
userInput = 0
twitterInput = ""
twitterLookup = ""
gnlaResults = []
debugAllValues = []
calcScoreResults = 0.0
userResults = ""
knownGood = ["#TheCrown","#BlackMirror","#Unbelievable","#TopBoy","#StrangerThings","#MindHunter","@Stranger_Things","@blackmirror","@disenchantment","@WhenTheySeeUs","@darkcrystal","@TheCrownNetflix"]

# Function to validate user input as a valid, well-known # or @ #
def InputValidation(t):
    results = "valid"
    # First, check for # / @ in first position
    if t[0:1] != "@" and t[0:1] != "#": results = "invalid"  # bad value, return "invalid"
    # Then, check value against list of known-good values
    if t not in knownGood: results = "invalid"  # bad value, return "invalid"
    return results

print("** Netflix original content sentiment analyzer **")
print("-------------------------------------------------")
print("There are 2 types of users: Netflix and Watcher")
print("(1) Netflix: for Netflix employees looking for a raw sentiment score (scale of 1-100)")
print("(2) Watcher: for Netflix viewers looking for show ratings (scale of 1-5 stars)")

userInput = input("\nEnter your user type (1 or 2) : ")
if userInput == "1": userType = "Netflix"
if userInput == "2": userType = "Consumer"

print("\nList of show #hashtags and @handles allowed: ")
print("----------------------------------------------")
print("{}, {}".format(", ".join(knownGood[:-1]), knownGood[-1]))

while(True):
    twitterInput = input("\nEnter the #hashtag or @handle you want to lookup (include the # or @): ")
    twitterLookup = InputValidation(twitterInput)  # Call function to validate input and check it's a valid entry
    if(twitterLookup != "invalid"):
        progTotal = 103  # Total number of items to be completed for the Progress Bar; assumes 100 tweets returned...
        i = 1  # Initialize Progress Bar counter
        PR.progress(i, progTotal, status='Collecting Tweets...')  # First iteration of Progress Bar (indicating start of all tasks)
        twitterResults = Get_twitter(twitterInput)  # Get Tweets based on input # / @
        #twitterResults = ["test","test","test","test","test","test","test","test","test","test"]
        i += 1  # Iterate Progress Bar counter
        totalTweets = len(twitterResults)  # Get count of Tweets returned
        if totalTweets == 0:
            PR.progress(progTotal, progTotal, status='Collecting Tweets...')  # Close out Progress Bar
            print("\n!! NO TWEETS RETURNED !! Please enter another #hashtag or @handle from the list above, including the # or @.")
        else:
            j = 0
            while j < totalTweets:  # Continue to iterate Progress Bar while getting Tweet sentiments
                PR.progress(i, progTotal, status='Analyzing Tweets...')
                time.sleep(0.1)
                gnlaReturn = GNL.GetSentiment(twitterResults[j])
                debugAllValues.append(gnlaReturn[:])
                del gnlaReturn[0]
                del gnlaReturn[0]
                gnlaResults.append(gnlaReturn[:])
                #gnlaResults.append(GNL.GetSentiment(twitterResults[j]))
                i += 1
                j += 1
            calcScoreResults = BL.CalcScore(gnlaResults)  # Send sentiment scores array to Business Logic unit for calculations; get float back
            userResults = BL.UserScore(userType, calcScoreResults)  # Send sentiment scores float to Business Logic unit to calculate score to return to user
            PR.progress(progTotal, progTotal, status='Analyzing Tweets...')  # Close out Progress Bar
            print("\nResults for {}: {}".format(twitterInput, userResults))
            #print("DEBUG:")
            #print(debugAllValues)
            import csv
            with open("test.csv", 'w', encoding='utf-8') as f:
               writer = csv.writer(f, delimiter=',')
               writer.writerows(debugAllValues)  #considering debugAllValues is a list of lists.
    else:
        print("!! Invalid entry !! Please enter a #hashtag or @handle from the list above, including the # or @.")


# Outline of steps:
# 0. Ask for user type (Netflix or watcher)
# 1. Ask user for # or @ to look-up
# 2. Call Twitter API to get back list of tweets in timeframes
#   - How do we know date of release for show to set timeframes? Ask for that as well?
#   - Return tweet text results stripped out of JSON API result as array of strings (or save to local file?)
# 3. Call Google API to analyze each tweet in subset
#	- Return sentiment and magnitude
#	- Store returned values in array/object
# 4. Call function to convert sentiments and magnitudes into overall sentiment values
# 5. Display results
