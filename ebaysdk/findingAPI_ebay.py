import ebaysdk
from ebaysdk.finding import Connection as Finding
from dateutil import parser

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

price = []
time = []
for item in dictstr['searchResult']['item']:
    print "ItemID: %s" % item['itemId']
    print "Title: %s" % item['title']
    print "URL: %s" % item['galleryURL']
    print "StartTime: %s" % item['listingInfo']['startTime']
    print "endTime: %s" % item['listingInfo']['endTime']
    print "Price: %s\n" % item['sellingStatus']['currentPrice']['value']
    price.append(float(item['sellingStatus']['currentPrice']['value']))
    datetime = item['listingInfo']['startTime'].split("T")
    #print type(datetime[0])
    time.append(parser.parse(datetime[0]))

print len(dictstr['searchResult']['item'])

