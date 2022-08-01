import pymongo

client = pymongo.MongoClient("mongodb+srv://mongo:mongo@mongo.mq2ji.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)

d= {'name':'neha','email':'jneha@gmail.com','surname':'joshi'}
db1= client['mongotest']
coll = db1['test1']
coll.insert_one(d)




