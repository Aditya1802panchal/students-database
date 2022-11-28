from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

total_avg=db.total_avg

# 4)Find the total and average of the exam, quiz and homework and
#  store them in a separate collection

data = collection.aggregate([
    {"$unwind": "$scores"},
    {"$group":
        {
            "_id": "$_id",
            "name": {"$first": "$name"}
            ,
            "Total": {"$sum": "$scores.score"},
            "Average": {"$avg": "$scores.score"}
        }
    },
    {"$sort": {"_id": 1}}

])

data1 = []
for i in data:
    data1.append(i)
    print(i)

total_avg.insert_many(data1)
