from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Sort documents by 'age' in ascending order
sorted_docs = collection.find().sort('age', 1)  # 1 for ascending, -1 for descending
for doc in sorted_docs:
    print(doc)

    # Delete a document where 'name' is 'John'
result = collection.delete_one({'name': 'John'})
print(f'Deleted {result.deleted_count} document(s).')

# Drop the collection
collection.drop()
print("Collection dropped.")

# Update a document where 'name' is 'Jane' and set her age to 30
result = collection.update_one({'name': 'Jane'}, {'$set': {'age': 30}})
print(f'Updated {result.modified_count} document(s).')

# Retrieve only 5 documents
limited_docs = collection.find().limit(5)
for doc in limited_docs:
    print(doc)