# 🌦 Weather 

Простое Django-приложение для получения текущей погоды по названию города. История запросов сохраняется в базе данных PostgreSQL.

## Установка и запуск

### 1. Клонирование репозитория

git clone https://github.com/tiliguzova/weather.git  
cd weather

### 2. Создание виртуального окружения

python -m venv venv  
source venv/bin/activate

### 3. Создание виртуального окружения

pip install -r requirements.txt

### 4. Создай файл .env в корне проекта со следующим содержанием

WEATHER_API_KEY=ваш_ключ
DB_NAME=имя_вашей_базы_данных
DB_USER=имя_пользователя_PostgreSQL
DB_PASSWORD=ваш_пароль_от_PostgreSQL
DB_HOST=localhost
DB_PORT=5432

### 5. Установи PostgreSQL и создай базу данных

CREATE DATABASE db;

### 5. Примени миграции и запусти сервер

python manage.py makemigrations  
python manage.py migrate  
python manage.py runserver

### Приложение

![Альтернативный текст](../static/images/home.png)  
![Альтернативный текст](../static/images/history.png)
