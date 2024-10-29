#  Extra: Read from log file and clean data.
# Looking at a log file from a webserver.


import pandas as pd
import matplotlib as plt 

# Read an assess.log file into a dataFrame (assume the delimiter is ‘ ‘)
path = '../data/'
logFilename = path + 'access.log.demo'
# df = pd.read_csv(logFilename, sep=' ', header= None) ================ this is changed in the following code down!

# It would be good to have meaningful column names, so change the read_csv (I
# looked up what each column means at apache.org, as you can see the file has ip
# addresses, timestamps, urls and lots of data from users accessing a web site
colNames= (
    'ip',
    'dash1',
    'userId',
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)
print(df)


# Check if it works by printing the first line (index 0).
print(df.iloc[0])

# Drop the columns that contain just dashes, (if the webserver is set up for userIds
# you may not want to do this).
df.drop(columns=['dash1', 'userId'], inplace=True)

import re 

# The time looks badly formatted let’s remove the [] and change the type of the
# column to data time. The apply function is handy for this.
# remove the [] from time
# there is a lot in this line
# apply with apply the function to each element in the column and return
# a series
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
# for the task you may want to use a normal function instead of lambda

'''
def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue
df['time'] = df['time'].apply(getNewValue)
'''

# Checking the column types.
print (df.dtypes)

# Change the type of the time column to dateTime
# this is not a normal date time format so we need to specify it
# https://docs.python.org/3/library/datetime.html#strftime-andstrptime-behavior
# https://pandas.pydata.org/pandasdocs/stable/reference/api/pandas.to_datetime.html?highlight=to_datetime
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

##############################################################################################
############################### A N A L Y S I S ##############################################
##############################################################################################

# Get the events that happened between two times
# way one use the loc function
# newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
# way 2 use the series function between
#newdf = df[df.time.between(start_date, end_date)]
# way three set the index to the date column
# this give a whole pile of handy features
df = df.set_index(['time'])
# newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
newdf = df.between_time('23:00', '23:59') # this is times every day.
print (newdf)

# Get mean amount of data that was downloaded every half an hour.
# sample the download sizes say every 30 Minutes
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# 6. Plot this in line plot.
# more information on the documents
# https://pandas.pydata.org/pandasdocs/stable/getting_started/intro_tutorials/04_plotting.html
downloadSamples.plot()
plt.show()