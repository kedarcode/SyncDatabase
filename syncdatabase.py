import pymongo


def createConn(client, database, collection):
    myclient = pymongo.MongoClient(client)
    mydb = myclient[database]
    mycol = mydb[collection]
    return mycol


db1 = createConn("mongodb://localhost:27017/", "syncdatabae1", "items")

db2 = createConn("mongodb://localhost:27017/", "syncdatabae2", "items2")

data1 = db1.find()

for item in data1:
    itemid = item['itemId']
    for stock in item['stock']:

        target_query = {"itemId": itemid, "refId": stock['itemReferenceCode']}
        target = db2.find_one(target_query)

        if target is None:
            item['stock'] = stock
            item['refId'] = stock['itemReferenceCode']
            db2.insert_one(item)
            print('missing', stock["stock"], {"itemId": itemid, "refId": stock['itemReferenceCode']})

        elif stock["stock"] != target['stock']['stock']:
            print('stcokchhange', stock["stock"], target['stock']['stock'],
                  {"itemId": itemid, "refId": stock['itemReferenceCode']})
            target['stock']['stock']=stock['stock']
            newvalues = {"$set": {"stock": target['stock']}}
            x = db2.update_one(target_query, newvalues)
