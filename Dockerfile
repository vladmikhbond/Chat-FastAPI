# Вихідний Python образ
FROM python:3.12-slim

# Встановити оновлення та системні залежності
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Встановити pip та pipx для ізольованої інсталяції
RUN pip install --upgrade pip

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо файли проєкту
COPY . .

# Встановлюємо залежності з pyproject.toml
RUN pip install .  # Встановить як пакет із pyproject.toml

# Відкриваємо порт
EXPOSE 8000

# Команда запуску сервера
CMD ["uvicorn", "chat.main:app", "--host", "0.0.0.0", "--port", "8000"]
