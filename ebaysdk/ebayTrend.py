from ebaysdk.finding import Connection as Finding
from dateutil import parser
import pylab

def getHistoricalPoints(keywords):
    api = Finding(siteid='EBAY-US', appid="JennyHun-7ae2-4c50-abd7-3c1af9cedea5")
    api.execute('findCompletedItems', {
        'keywords': 'Willow Tree shepherd',
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
    Hprice = []
    Htime = []    
    for item in dictstr['searchResult']['item']:
        print "ItemID: %s" % item['itemId']
        print "Title: %s" % item['title']
        print "CategoryID: %s" % item['primaryCategory']['categoryId']
        #print "URL: %s" % item['galleryURL']
        print "StartTime: %s" % item['listingInfo']['startTime']
        print "endTime: %s" % item['listingInfo']['endTime']
        print "SoldPrice: %s\n" % item['sellingStatus']['currentPrice']['value']
        Hprice.append(float(item['sellingStatus']['currentPrice']['value']))
        datetime = item['listingInfo']['startTime'].split("T")
        Htime.append(parser.parse(datetime[0]))        
    print len(dictstr['searchResult']['item'])
    return (Hprice, Htime)
    print Hprice    
    

def getCurrentPoints(keywords):
    api = Finding(siteid='EBAY-US', appid="JennyHun-7ae2-4c50-abd7-3c1af9cedea5")
    api.execute('findItemsAdvanced', {
        'keywords': 'willow tree shepherd',
        #'categoryId' : ['177', '111422'],
        'itemFilter': [
            {'name': 'Condition', 'value': 'Used'},
            #{'name': 'MinPrice', 'value': '10', 'paramName': 'Currency', 'paramValue': 'USD'},
            #{'name': 'MaxPrice', 'value': '30', 'paramName': 'Currency', 'paramValue': 'USD'}
        ],
        'paginationInput': {
            'entriesPerPage': '3000',
            'pageNumber': '1' 	 
        },
        'sortOrder': 'CurrentPriceHighest',
        #'outputSelector': 'pictureURLLarge'
    })
    dictstr = api.response.dict()
    #print dictstr
    Cprice = []
    Ctime = []
    for item in dictstr['searchResult']['item']:
        print "ItemID: %s" % item['itemId']
        print "Title: %s" % item['title']
        print "URL: %s" % item['galleryURL']
        print "StartTime: %s" % item['listingInfo']['startTime']
        print "endTime: %s" % item['listingInfo']['endTime']
        print "AskingPrice: %s\n" % item['sellingStatus']['currentPrice']['value']
        Cprice.append(float(item['sellingStatus']['currentPrice']['value']))
        datetime = item['listingInfo']['startTime'].split("T")
        Ctime.append(parser.parse(datetime[0]))
    print len(dictstr['searchResult']['item'])
    return (Cprice, Ctime)
    
    
def graphAllPoints(keyword):
    Hprice_array = pylab.array(getHistoricalPoints(keyword)[0])
    Htime_array = pylab.array(getHistoricalPoints(keyword)[1])
    Cprice_array = pylab.array(getCurrentPoints(keyword)[0])
    Ctime_array = pylab.array(getCurrentPoints(keyword)[1])
    pylab.title("Willow Tree shepherd, HistoricalPoints and CurrentPoints")
    pylab.xlabel("Time")
    pylab.ylabel("Price")
    pylab.plot(Htime_array, Hprice_array, "ro", label = "Historical")
    pylab.plot(Ctime_array, Cprice_array, "b^", label = "Current")
    pylab.legend(loc = "upper left")
    #pylab.plot(Htime_array, Hprice_array, "ro", Ctime_array, Cprice_array, "b^")
    pylab.show()


#getHistoricalPoints("Willow Tree shepherd")
getCurrentPoints("willow tree shepherd")
graphAllPoints("will tree sheperd")