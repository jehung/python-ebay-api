from ebaysdk.shopping import Connection as Shopping
try:    
    api = Shopping(appid="JennyHun-7ae2-4c50-abd7-3c1af9cedea5")
    response = api.execute('FindPopularItems', {'QueryKeywords': 'willow tree creche'})
    print(response.dict())
    print(response.reply)
except: 
    print "error"





#ConnectionError as e:
#    print(e)
#    print(e.response.dict())