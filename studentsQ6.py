from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

# Q6)Create a new collection which consists of students
# who scored below the fail mark in all the categories

fail = db.fail

query = {}
data = collection.aggregate(
    [{"$match":
          {"$expr":

               {"$lt": [{"$max": "$scores.score"}, 40]}

           }
      }])

faila = []
for i in data:
    faila.append(i)
    print(i)

fail.insert_many(faila)