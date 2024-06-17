import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, ValidationError
from bson import ObjectId
from typing import List, Optional


class MessageModels(BaseModel):
    id: Optional[str] = Field(alias="_id")
    messages: List[dict] = [{
        "role": "system",
        "content": "Ты виртуальный консультант 'Окси', ты помогаешь составлять статьи для телеграмм каналов и подсказываешь что тут и как. "
                   "Твой создатель: Романейко Илья"
    }]

    class Config:
        json_encoders = {
            ObjectId: str
        }


# Функция для конвертации данных из MongoDB в Pydantic модель
def message_model_from_mongo(data):
    return MessageModels(**data)


# Метод для поиска документа по id и добавления нового сообщения в поле messages
async def add_message_by_id(client, collection_name, document_id, new_message):
    # Подключаемся к коллекции
    db = client.mydatabase
    collection = db[collection_name]

    # Ищем документ по ID
    found_message = await collection.find_one({"_id": ObjectId(document_id)})
    if found_message:
        # Конвертируем найденный документ в модель
        message_model = message_model_from_mongo(found_message)
        print('Found document:', message_model)

        # Добавляем новое сообщение в поле messages
        message_model.messages.append(new_message)

        # Обновляем документ в базе данных
        await collection.update_one(
            {"_id": ObjectId(document_id)},
            {"$set": {"messages": message_model.messages}}
        )

        # Проверяем обновление
        updated_message = await collection.find_one({"_id": ObjectId(document_id)})
        if updated_message:
            updated_message_model = message_model_from_mongo(updated_message)
            print('Updated document:', updated_message_model)
    else:
        print(f"No document found with id: {document_id}")


# Пример использования метода
async def main():
    client = AsyncIOMotorClient('mongodb://localhost:27017')

    # ID документа, который мы будем обновлять
    document_id = "60c72b2f9f1b2c001f8e4e3b"  # замените на реальный ID вашего документа

    # Новое сообщение, которое нужно добавить
    new_message = {
        "role": "user",
        "content": "Новое сообщение от пользователя."
    }

    await add_message_by_id(client, 'messages', document_id, new_message)

    # Закрываем соединение
    client.close()


# Запуск асинхронного цикла событий
asyncio.run(main())
