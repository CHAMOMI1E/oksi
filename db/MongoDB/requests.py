from motor import motor_asyncio
import asyncio

from db.MongoDB.models import MessageModels

from config import MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT

# Замените на ваши значения


# Создание клиента MongoDB
client = motor_asyncio.AsyncIOMotorClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}")
db = client.test_db

# Connect to the 'test_collection' collection
collection = db.test


async def add_message():

    message = MessageModels(messages=[{"role": "user", "content": "Hello, world!"}])
    result = await collection.insert_one(message.dict())
    print(f"Inserted document with ID: {result.inserted_id}")




if __name__ == '__main__':
    asyncio.run(add_message())
