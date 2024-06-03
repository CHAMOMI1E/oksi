from dotenv import load_dotenv
import os

# Загрузить переменные из файла .env в переменные окружения
load_dotenv()


TOKEN_TEST = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANEL_ID')