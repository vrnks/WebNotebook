# WebNotebook
![image](https://github.com/vrnks/WebNotebook/assets/130937932/3940edac-fa01-49d4-93c6-6df5bc4cd364)

Інструкція встановлення: 
- Клонуйте репозиторій проекту з GitHub: https://github.com/vrnks/WebNotebook
- Встановіть PostgreSQL і створіть базу даних для проекту.
- Заповніть файл .env
- Запустіть міграцію бази даних для створення необхідних таблиць: python manage.py makemigrations; python manage.py migrate. Запустіть сервер розробки Django: python manage.py runserver Запустіть додаток через веб-браузер за адресою http://localhost:8000/.

Структура проекту. note/: Містить конфігураційні файли проекту Django (asgi.py, settings.py, urls.py, wsgi.py тощо). noteapp/: Містить застосунок Django з основним функціоналом додатку "Нотатки". templates/: Зберігає HTML-шаблони для візуалізації подання. static/: Зберігає статичні файли, такі як CSS та інше. manage.py: Скрипт керування проектом Django.

Інструкція використання проєкту. Notebook: Для додавання котатки чи тегів використувуємо кнопки Add note та Add Tag відповідно. Додавання тегу здійснюється введенням назви та підтвердженням. Додавання нотатки здійснюється введенням назви, опису, обиранням тегів та підтвердженням. Щоб видалити чи змінити нотатку використовуються кнопки delete note чи edit note відповідно. Містить функціонал пошуку та сортуванням нотаток за певним тегом. 
