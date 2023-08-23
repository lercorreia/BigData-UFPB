from pymongo import MongoClient
import sys
import json

client = MongoClient("mongodb+srv://dev:EIhYcyK6shA9qPgn@bigdataanalytics.zyl9tkj.mongodb.net/app1")
db = client['app1']
tweet = db['tweet']

#retorna os atributos do primeiro documento encontrado
searchResult = tweet.find_one()
print(searchResult)

# O hasOwnProperty() pode ser implementado no mongodb, utilizando o método find e o operador "$exists"
# Como mostado abaixo:

#busca por atributo existente
searchResult = tweet.find({'created_at':{'$exists': True}})

#Busca por atributo inexistente
searchResult2 = tweet.find({'dsadsa':{'$exists': True}})

print("Atributo existente ", len(list(searchResult)))
print("Atributo não existente ", len(list(searchResult2)))

#Busca com agregate para encontrar as 10 hashtags mais utilizadas
searchResult = tweet.aggregate([{"$match": {"entities.hashtags.text":{"$exists":True, "$ne":""}}},{"$group":{"_id": "$entities.hashtags.text", "count":{"$sum":1}}}, {"$sort":{"count":-1}}, {"$limit":10}])

# Mostra as hashtags mais usadas, retirando as hashtags vazias 
for documentos in searchResult:
    print(documentos)