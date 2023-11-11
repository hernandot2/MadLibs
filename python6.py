from pymongo import MongoClient
connection_string = "mongodb://admin:password@localhost:27017/?authSource=admin"
cliente = MongoClient(connection_string)
db_connection = cliente['Hcode']

print(db_connection)