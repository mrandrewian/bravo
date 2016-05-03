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

#data repo
allData=[]
# create fastesttime var -- this will update as i find KoMs
	# what should initial fastest time be? maybe just a huge number so the first one i see is a KoM. this seems to work
	# lets set it at 60000 = 1000 minutes
fastestTime=60000
# loop over multiple pages from API
for i in range(2):
	# create page variable
	pag=str(i+1)
	# create url with varying page variable
	url=strava+'segments/'+segId+'/all_efforts?'+'access_token='+apiToken+'&start_date_local='+startDate+'&end_date_local='+endDate+'&per_page='+perPage+'&page='+pag
	# request
	a=requests.get(url)
	# create json object
	jsonifiedData=a.json()
	# pull out data i want using for loop. use if statement to find fastest times
	# loop through all records and check if next time is a KoM. if so, add to list effort
	for i in range(len(jsonifiedData)):
		effort=[]
		# check if time under consideration is faster than current fastest time recorded. if so, record time and start date
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
