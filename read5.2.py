import urllib2,json,base64
accesstoken = "LAF4MNPN2J57W4MRUTT9"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json?pageIndex={}".format(
    institution,
    course,
    page
    )
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
x = data[6]
a = x["Details"]
c = a[1]
print c["Value"]

