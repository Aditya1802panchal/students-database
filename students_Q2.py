from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

#2)Find students who scored below average in the exam and pass mark is 40%?
query = {'scores.type': 'exam', 'scores.score': {'$gt': 40, '$lt': 60}}

data = collection.aggregate([
    {'$unwind': '$scores'},
    {"$match": query}
])

for i in data:
    print(i)