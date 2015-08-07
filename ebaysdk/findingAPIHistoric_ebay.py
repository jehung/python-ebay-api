import ebaysdk
from ebaysdk.finding import Connection as Finding
import pylab
#import rpy2
from dateutil import parser

api = Finding(siteid='EBAY-US', appid="JennyHun-7ae2-4c50-abd7-3c1af9cedea5")
api.execute('findCompletedItems', {
    'keywords': 'willow tree shepherd',
    #'categoryId' : ['177', '111422'],
    'itemFilter': [
        {'name': 'Condition', 'value': 'Used'},
        {'name': 'MinPrice', 'value': '0', 'paramName': 'Currency', 'paramValue': 'USD'},
        {'name': 'MaxPrice', 'value': '3000', 'paramName': 'Currency', 'paramValue': 'USD'}
    ],
    'paginationInput': {
        'entriesPerPage': '2000',
        'pageNumber': '1' 	 
    },
    'sortOrder': 'CurrentPriceHighest',
})

dictstr = api.response.dict()
price = []
time = []

for item in dictstr['searchResult']['item']:
    print "ItemID: %s" % item['itemId']
    print "Title: %s" % item['title']
    print "CategoryID: %s" % item['primaryCategory']['categoryId']
    print "URL: %s" % item['galleryURL']
    print "StartTime: %s" % item['listingInfo']['startTime']
    print "endTime: %s" % item['listingInfo']['endTime']
    print "SoldPrice: %s\n" % item['sellingStatus']['currentPrice']['value']
    price.append(float(item['sellingStatus']['currentPrice']['value']))
    datetime = item['listingInfo']['startTime'].split("T")
    print type(datetime[0])
    time.append(parser.parse(datetime[0]))
    
#print time
    
print len(dictstr['searchResult']['item'])
#print price
#
#pylab.array(price)  ##This is the python code to graph a histogram
#pylab.plot(time, price, "ro")
#pylab.hist(price)
#pylab.show()
##################################################################
# TODO: import R and use R code to do time-series analysis
#from numpy import *
#import scipy as sp
#from pandas import *
#import rpy2.robjects as ro
#from rpy2.robjects.packages import importr
#import rpy2.robjects as ro
#import pandas.rpy.common as com

import pandas as pd
import pyper
from pyper import *
r = R(RCMD="C:\\Program Files\\R\\R-3.1.2\\bin\\R")
#r = pyper.R(use_pandas = True)
r.assign("rprice", price)
print r("summary(rprice)")
print r("mean(rprice)")
print r("sd(rprice)")