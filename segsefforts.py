import secrets
import requests
import pandas as pd

## get segment urls
def segments(idlist):
	# time params
	startDate='2010-01-01T00:00:00Z'
	endDate='2015-05-01T00:00:00Z'
	# final urls execpt for page and perpage will go in this list
	urlsMinusPage=[]
	# go through all seg ids to make urls
	for i in range(len(idlist)):
		u='https://www.strava.com/api/v3/'+'segments/'+idlist[i]+'/all_efforts?'+'access_token='+secrets.apiToken+'&start_date_local='+startDate+'&end_date_local='+endDate
		urlsMinusPage.append(u)	
	return urlsMinusPage

# this code returns segment urls
#a=segments(['673849','825464','188'])

# get json of all efforts for segments
def allefforts(u):
	# this is where all efforts will go 
	allData=[]
	# set number of results per page
	perPage='20'
	# do this for each url. len(u) = number of seg ids
	for i in range(len(u)):
		urlsMinusPage=u[i]+'&per_page='+perPage+'&page='
		# singleseg is where we will drop data for 1 segment
		singleseg=[]
		# go to multiple pages
		for k in range(5):
			# create page variable
			pag=str(k+1)
			# create url with varying page variable
			url=urlsMinusPage+pag
			# request
			a=requests.get(url)
			# create json object
			jsonifiedData=a.json()
			# all all this to all data
			singleseg.append(jsonifiedData)
		# put data for all of 1 segment into bigger list called alldata	
		allData.append(singleseg)
	return allData
	
# first gets in
# second references all whirls
# third is first effort for whirls
# then look at elapsed time
#print(b[0])# this just prints all whirlwinds > list of length = however many pages we spit out >> number of pages
#print(len(b[0][0])) # this is list of 20 efforts per page >> efforts per page
#print(b[0][0][0]) # this is a single effort
#print(b[0][0][0]['average_watts'])# this prints data we want


#################################
#################################
# so it goes list of pages > list of efforts per page > single effort > data from an effort

###########
########


def koms(js):
 	#fastestTime=100000
	allData=[]
	for i in range(len(js)): # this is n for n segments...find all KoM list for all segments:
		# check if time under consideration is faster than current fastest time recorded. if so, record time and start date
		oneseg=[]
		#set max time 
		fastestTime=100000
		# for each page
		for k in range(len(js[i])):
			# for results on page (perpage)
			for l in range(len(js[i][k])):
				# if statement to find KoMs
				if js[i][k][l]['elapsed_time']< fastestTime:
					oneseg.append(js[i][k][l]['elapsed_time'])
					oneseg.append(js[i][k][l]['start_date_local'])
					oneseg.append(js[i][k][l]['name'])
					fastestTime=js[i][k][l]['elapsed_time']
		allData.append(oneseg)
	return allData


#execute
a=segments(['673849','825464','188'])
b=allefforts(a)
c=koms(b)

# reformat arrays
x=pd.Series(c)

print(x)

# print to csv for analysis in r. probably some way to just talk to R from python, but i dont know
x.to_csv('foo.csv')
