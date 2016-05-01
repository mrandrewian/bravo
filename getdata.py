import requests

# api request

# parameters
segId='673849'
apiToken='f6dc55288ccd2ca77c2e4f54a1009aec09c37eb9'
startDate='2015-01-01T00:00:00Z'
endDate='2016-01-01T00:00:00Z'
strava='https://www.strava.com/api/v3/'
perPage='5'
page='1'

# build url
url=strava+'segments/'+segId+'/all_efforts?'+'access_token='+apiToken+'&start_date_local='+startDate+'&end_date_local='+endDate+'&per_page='+perPage+'&page='+page

# request
a=requests.get(url)

# create json object
jsonifiedData=a.json()


# pull out data i want using for loop
allData=[]
for i in range(len(jsonifiedData)):
	effort=[]
	effort.append(jsonifiedData[i]['average_watts'])
	effort.append(jsonifiedData[i]['elapsed_time'])
	allData.append(effort)

print allData
