# Приложение для сбора вакансий

Это Django-приложение для сбора вакансий с использованием парсеров. 
Оно использует Celery для асинхронных задач и Postgres в качестве базы данных. 
Весь проект упакован в Docker Compose для удобства развертывания и управления.

## Технологии

- Django
- Celery
- Celery Beat
- PostgreSQL
- Redis (в качестве брокера сообщений для Celery)
- Docker
- Django REST framework 
- Docker Compose
- Requests
- BeautifulSoup

## Установка и запуск

1. Клонируйте репозиторий:git clone https://github.com/Aliaksandrsw/Job_parser
2. Перейдите в директорию проекта Job_parser
3. Создайте файл .env из примера .env.example
4. Настройте переменные окружения в файле .env
5. Соберите и запустите проект с помощью Docker Compose: docker-compose up --build
6. Приложение будет доступно по адресу `http://localhost:8000` (или другому порту, если вы изменили настройки).

## Использование

Данное приложение собирает воедино вакансии по python с разных площадок по поиску работы
