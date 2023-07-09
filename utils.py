import pymongo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# set up a conninsection to MongoDB
client = pymongo.MongoClient("mongodb+srv://gabrielrosendo72:IkowGwDys5bRfSn0@boats.xc4of4g.mongodb.net/")

# specify the database and collection you want to insert data into
db = client["boats"]
collection = db["boats-sale"]

# create a dictionary with the data you want to insert
results = collection.find()
boats_sale =[]
for boat in results:
   boats_sale.append(boat)

# Print the retrieved data
for boat in boats_sale:
    print(boat)

# Close the connection
client.close()