from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMIN_ID = env.str("admin_id")  # Тут у нас будет список из админов

API_KEY = env.str("API_KEY")