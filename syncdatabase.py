import pymongo
import requests


def createConn(client, database, collection):
    myclient = pymongo.MongoClient(client)
    mydb = myclient[database]
    mycol = mydb[collection]
    return mycol


db1 = requests.get(
    'http://siddhiartjewellery.true-order.com/WebReporter/api/v1/items?locationId=%3D2&limit=30000&selectAll=true',
    headers={'Content-Type': ''
                             'application/json;charset=UTF-8',
             'X-Auth-Token': '20D48FEA0700964D5FF5A51519F925D464D862798609188500AB67277A82E796FE7A104D6C57DDAB'})
data1 = db1.json()['items']
db2 = createConn("mongodb://localhost:27017/", "syncdatabae2", "items2")
for item in data1:
    itemid = item['itemId']
    for stock in item['stock']:
        target_query = {"itemId": itemid, "refId": stock['itemReferenceCode']}
        target = db2.find_one(target_query)
        if target is None:
            if '_id' in stock:
                del stock['_id']
            if '_id' in item:
                del item['_id']

            item['stock'] = stock
            item['refId'] = stock['itemReferenceCode']

            db2.insert_one(item)
            # print('missing', stock["stock"], {"itemId": itemid, "refId": stock['itemReferenceCode']})

        elif stock["stock"] != target['stock']['stock']:
            # print('stcokchhange', stock["stock"], target['stock']['stock'],
            #       {"itemId": itemid, "refId": stock['itemReferenceCode']})
            target['stock']['stock'] = stock['stock']
            newvalues = {"$set": {"stock": target['stock']}}
            x = db2.update_one(target_query, newvalues)
