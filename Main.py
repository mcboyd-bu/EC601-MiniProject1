import GoogleNatLangAPI as GNL
import plotly.graph_objects as go
import time

#g = raw_input("Enter your name : ")  # Python 2.x Version
g = input("Enter your name : ")  # Python 3.x version
print(g)

#fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
#fig.write_html('first_figure.html', auto_open=True)
#test = GNL.GetSentiment('Hello world, this is a test')
#print(test)


# Outline of steps:
# 1. Ask user for # or @ to look-up
# 2. Call Twitter API to get back list of tweets in timeframes
#   - How do we know date of release for show to set timeframes? Ask for that as well?
#   - Return tweet text results stripped out of JSON API result as array of strings (or save to local file?) 
# 3. Call function to (randomly) extract a subset of the tweets for analysis (certain number per day, maybe?)
#	- Return as array/text file
# 4. Call Google API to analyze each tweet in subset
#	- Return sentiment and magnitude
#	- Store returned values in array/object
# 5. Call function to convert sentiments and magnitudes into overall daily sentiment values
# 6. Call library to plot chart of daily values
#	- Plotly: https://plot.ly/python/getting-started/
#
# ! Probably use ProgressBar2 to display progress for user as the many above tasks are happening...
# ! https://pypi.org/project/progressbar2/