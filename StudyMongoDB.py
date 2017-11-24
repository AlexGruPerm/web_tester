from pymongo import MongoClient
from datetime import datetime

mon_user = ""
mon_pass = ""
mon_db = "test_db"

#mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
client = MongoClient("mongodb://localhost:27017")

print(client)
db = client[mon_db]

#print(db['dataset'])
#coll = db['dataset']
#print(coll)

result = db.rest.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

print(result.inserted_id)

cursor = db.rest.find()

for document in cursor:
    print(document)

print("----------------------")

cursor = db.rest.find({'borough': 'Manhattan'})

for document in cursor:
    print(">>>  ", document)
