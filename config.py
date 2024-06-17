from dotenv import load_dotenv
import os

# Загрузить переменные из файла .env в переменные окружения
load_dotenv()

TOKEN_TEST = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANEL_ID')
DB_TOKEN = os.getenv('DB_TOKEN')

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = os.getenv('MONGO_PORT')
MONGO_USER = os.getenv('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASS = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
