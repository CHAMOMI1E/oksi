from typing import Optional, List

from bson import ObjectId
from motor import motor_asyncio

from pydantic import BaseModel, Field

from config import MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT

# Замените на ваши значения


# Создание клиента MongoDB
client = motor_asyncio.AsyncIOMotorClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}")
db = client.test_db

message_collection = db.test


class MessageModels(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    messages: List[dict] = [{
        "role": "system",
        "content": "Ты виртупльный консултанат 'Окси', ты помогаешь составлять статьи для телеграмм каналов и подсказываешь что тут и как"
                   "Твой создатель: Романейко Илья"}, ]

    class Config:
        json_encoders = {
            ObjectId: str
        }

