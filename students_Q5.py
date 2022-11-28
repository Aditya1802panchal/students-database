from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

# Q5)Create a new collection which consists of students
#  who scored below average and above 40% in all the categories

Avgrage_Candidates = db.Avgrage_Candidates

data = collection.aggregate(
    [{"$match":
          {"$expr":
               {"$and":
                    [{"$gt": [{"$min": "$scores.score"}, 40]},
                     {"$lt": [{"$max": "$scores.score"}, 70]}
                     ]
                }
           }
      }])

Data1 = []
for i in data:
    Data1.append(i)
    print(i)

Avgrage_Candidates.insert_many(Data1)