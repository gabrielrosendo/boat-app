import pymongo
import certifi
ca = certifi.where()

# set up a connection to MongoDB
client = pymongo.MongoClient("mongodb+srv://[hidden]/", tlsCAFile=ca)

db = client["boats"]
sale_collection = db["boats-sale"]
charter_collection = db["boats-charter"]

results_sale = sale_collection.find()
boats_sale =[]
for boat in results_sale:
   boats_sale.append(boat)

results_charter = charter_collection.find()
boats_charter = []
for boat in results_charter:
   boats_charter.append(boat)
   

# Close the connection
