
Этот сервис позволяет загружать рекламные площадки из файла и искать подходящие площадки для заданной локации.

# Инструкция по запуску.

## Запуск с помощью Docker

1. Соберите Docker-образ:
   ```bash
   docker build -t ad_service .
2. Запустите контейнер:
   ```bash
   docker run -d -p 8000:8000 ad_service
3. API будет доступно по адресу: 
   http://localhost:8000.
## API Endpoints
### POST /upload/: Загружает данные из файла.
* curl -X POST -F "file=@data.csv" http://localhost:8000/upload/

### GET /search/: Ищет рекламные площадки для заданной локации.
* curl -X GET "http://localhost:8000/search/?location=/ru/svrd/revda" 
# Запуск тестов
* python -m unittest discover -s tests


---

###  **`run.sh`** (опцонально)
#### Если вы используете Docker, то run.sh не понадобится, так как приложение будет запускаться через команду в Dockerfile.
Скрипт для удобного запуска приложения по команде
./run.sh
```bash
#!/bin/bash

# Запуск приложения с помощью uvicorn
uvicorn main.app:app --host 0.0.0.0 --port 8000