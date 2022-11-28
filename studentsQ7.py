from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

# Q7)Create a new collection which consists of students
#  who scored above pass mark in all the categories

passed = db.passed

query = {}
data = collection.aggregate(
    [{"$match":
          {"$expr":

               {"$gt": [{"$max": "$scores.score"}, 40]}

           }
      }])

passed1 = []
for i in data:
    passed1.append(i)
    print(i)

passed.insert_many(passed1)