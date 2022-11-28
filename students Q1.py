from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

#1)      Find the student name who scored maximum scores in all (exam, quiz and homework)?

data = collection.aggregate([
    {"$unwind": "$scores"},
    {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "Total": {"$sum": "$scores.score"}}},
    {"$sort": {"Total": -1}},
    {"$limit": 1}
])

for i in data:
    print(i)

