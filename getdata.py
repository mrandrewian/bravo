import requests
import secrets
import pandas as pd

# api request

# parameters
segId='673849'
apiToken=secrets.apiToken
startDate='2015-01-01T00:00:00Z'
endDate='2016-01-01T00:00:00Z'
strava='https://www.strava.com/api/v3/'
perPage='200'
page='1'

# build url
url=strava+'segments/'+segId+'/all_efforts?'+'access_token='+apiToken+'&start_date_local='+startDate+'&end_date_local='+endDate+'&per_page='+perPage+'&page='+page

# request
a=requests.get(url)

# create json object
jsonifiedData=a.json()


# pull out data i want using for loop. use if statement to find fastest times
allData=[]
fastestTime=jsonifiedData[0]['elapsed_time']
for i in range(len(jsonifiedData)):
	effort=[]
	if jsonifiedData[i]['elapsed_time']< fastestTime:
		effort.append(jsonifiedData[i]['start_date_local'])
		effort.append(jsonifiedData[i]['elapsed_time'])
		fastestTime=jsonifiedData[i]['elapsed_time']
	allData.append(effort)


# reformat arrays
x=pd.Series(allData)

print(x)

# print to csv for analysis in r. probably some way to just talk to R from python, but i dont know
#x.to_csv('foo.csv')
