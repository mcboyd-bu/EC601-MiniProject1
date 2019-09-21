import GoogleNatLangAPI as GNL
import BusinessLogic as BL
import time
from twitter_api import Get_twitter

userType = ""
userInput = 0
twitterInput = ""
twitterLookup = ""

print("** Netflix original content sentiment analyzer **")
print("There are 2 types of users: Netflix and Watcher")
print("(1) Netflix: for Netflix employees looking for a raw sentiment score (scale of 1-100)")
print("(2) Watcher: for Netflix viewers looking for show ratings (scale of 1-5 stars)")

#g = raw_input("Enter your user type (1 or 2) : ")  # Python 2.x Version
userInput = input("Enter your user type (1 or 2) : ")  # Python 3.x version
if (userInput == "1") userType = "Netflix"
if (userInput == "2") userType = "Watcher"
print(userInput)
print(userType)
print("List of show #hashtags and @handles allowed: ...")

while(true):
    twitterInput = input("Enter the #hashtag or @handle you want to lookup (include the # or @): ")
    # call function below to validate input and check it's a valid entry
    twitterLookup = InputValidation(twitterInput)
    print(twitterInput)
    print(twitterLookup)
    if(twitterLookup != "invalid"):
        print(Get_twitter(tag))
    else:
        print("Invalid entry, please enter a #hashtag or @handle from the list above, including the # or @.")

    # time = input("Enter the time in the form of YYYY-MM-DD : ")
    # print(time)



def InputValidation(t):
    results = "invalid"
    # check for # / @ in first position
    # check value against list of known-good values
    # bad value, return "invalid"
    return results

#test = GNL.GetSentiment('Hello world, this is a test')
#print(test)


# Outline of steps:
# 0. Ask for user type (Netflix or watcher)
# 1. Ask user for # or @ to look-up
# 2. Call Twitter API to get back list of tweets in timeframes
#   - How do we know date of release for show to set timeframes? Ask for that as well?
#   - Return tweet text results stripped out of JSON API result as array of strings (or save to local file?)
# NO MORE 3. Call function to (randomly) extract a subset of the tweets for analysis (certain number per day, maybe?)
# NO MORE	- Return as array/text file
# 4. Call Google API to analyze each tweet in subset
#	- Return sentiment and magnitude
#	- Store returned values in array/object
# 5. Call function to convert sentiments and magnitudes into overall daily sentiment values
# 6. Display results
# NO MORE 6. Call library to plot chart of daily values
# NO MORE	- Plotly: https://plot.ly/python/getting-started/
#
# ! Probably use ProgressBar2 to display progress for user as the many above tasks are happening...
# ! https://pypi.org/project/progressbar2/
