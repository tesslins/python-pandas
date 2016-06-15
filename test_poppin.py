import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# DataFrame (2D array) from array
starting_date = '2016-01-18'

dates = pd.date_range(starting_date, periods=6)
# dates: DatetimeIndex(['2016-01-18', '2016-01-19', '2016-01-20', '2016-01-21',
#                '2016-01-22', '2016-01-23'],
#               dtype='datetime64[ns]', freq='D')

frame = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

print frame

# DataFrame (2D array) from dict
event = {'_id' : {"$oid":"569d420925e7f9d8e8ca57a4"},
        'type':"initialRequest",
        'data':{
            'requestUrl':"localhost:3000/",
            'sessionId':"202aa041-356d-11e5-aeca-3d863e44f157",
            'ipAddress':"127.0.0.1",
            'userAgent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
            'dateCreated':{
                            '$date':"2016-01-18T19:50:33.868Z"}
                        },
        '__v':0}

events = {
            'event1' : {"_id":{"$oid":"569d420925e7f9d8e8ca57a4"},"type":"initialRequest","data":{"requestUrl":"localhost:3000/","sessionId":"202aa041-356d-11e5-aeca-3d863e44f157","ipAddress":"127.0.0.1","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36","dateCreated":{"$date":"2016-01-18T19:50:33.868Z"}},"__v":0}
,
            'event2' : {"_id":{"$oid":"569d420925e7f9d8e8ca57a5"},"type":"initialRequest","data":{"requestUrl":"localhost:3000/","sessionId":"202aa041-356d-11e5-aeca-3d863e44f157","ipAddress":"127.0.0.1","userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36","dateCreated":{"$date":"2016-01-18T19:50:33.959Z"}},"__v":0}
        }

frame2 = pd.DataFrame(events)

print frame2
print ""
print frame2.dtypes
