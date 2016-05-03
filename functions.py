import secrets
import requests


## get segment urls
def segments(idlist):
	startDate='2010-01-01T00:00:00Z'
	endDate='2011-05-01T00:00:00Z'
	urlsMinusPage=[]
	for i in range(len(idlist)):
		u='https://www.strava.com/api/v3/'+'segments/'+idlist[i]+'/all_efforts?'+'access_token='+secrets.apiToken+'&start_date_local='+startDate+'&end_date_local='+endDate
		urlsMinusPage.append(u)	
	return urlsMinusPage

# this code returns segment urls
x=segments(['673849','825464'])
print(x)

# get json of all efforts for segments
def allefforts(u):
	# this is where all efforts will go 
	allData=[]
	# set number of results per page
	perPage='5'
	# do this for each url
	for i in range(len(u)):
		urlsMinusPage=u[i]+'&per_page='+perPage+'&page='
		# singleseg is where we will drop data for 1 segment
		singleseg=[]
		# go to multiple pages
		for i in range(2):
			# create page variable
			pag=str(i+1)
			# create url with varying page variable
			url=urlsMinusPage+pag
			# request
			a=requests.get(url)
			# create json object
			jsonifiedData=a.json()
			# all all this to all data
			singleseg.append(jsonifiedData)
		allData.append(singleseg)
	return allData
	
print(allefforts(x))
