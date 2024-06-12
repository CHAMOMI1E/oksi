from pymongo import MongoClient

# Замените на ваши значения
mongo_host = "localhost"
mongo_port = 27018
username = 'chamomile'
password = "02082002"

# Создание клиента MongoDB
client = MongoClient(f"mongodb://{username}:{password}@{mongo_host}:{mongo_port}/?authSource=admin")
db = client.test_db  # Замените на ваше имя базы данных
collection = db.test_collection

document = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# # Вставка одного документа
# result = collection.insert_one(document)
# print(f"Inserted document ID: {result.inserted_id}")
#
# # Вставка нескольких документов
# documents = [
#     {"name": "Alice", "age": 25, "email": "alice@example.com"},
#     {"name": "Bob", "age": 27, "email": "bob@example.com"}
# ]
#
# result = collection.insert_many(documents)
# print(f"Inserted document IDs: {result.inserted_ids}")


document = collection.find({"age": {"$gt": 25}})
print("Пользователи старше 25 лет:")
for doc in document:
    print(doc)
