import os
import logging

# Определяем путь к файлу логов
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debug.log')

# Настраиваем логгирование
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Уровень логирования (может быть DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Создаем логгер для вашего приложения
logger = logging.getLogger('users')
