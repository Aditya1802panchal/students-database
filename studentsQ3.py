from pymongo import MongoClient
cli=MongoClient()
print(cli.list_database_names())
db=cli.studentsDB
print(db.list_collection_names())
collection=db.students_collection

# 3)=Find students who scored below pass mark and assigned them as fail,
# and above pass mark as pass in all the categories

data = collection.aggregate(
    [{"$set":
          {"scores":
               {"$arrayToObject":
                    [{"$map":
                          {"input": "$scores",
                           "as": "s",
                           "in": {"k": "$$s.type", "v": "$$s.score"}}}]}}},
     {"$project":
         {
             "_id": 1,
             "name": 1,
             "result": {
                 "$cond":
                     {"if": {"$and": [{"$gte": ["$scores.exam", 40]}, {"$gte": ["$scores.quiz", 40]},
                                      {"$gte": ["$scores.homework", 40]}]
                             },
                      "then": "pass",
                      "else": "fail"
                      }
             }
         }
     }
     ])

for i in data:
    print(i)