# fastapi_example
Пример испльзования FastAPI+PostgreSQL в Docker

# Эндпойнты:
- **/api/healthchecker** - get запрос, проверяющий состояние сервиса.
![healthcheck.jpeg](screenshots%2Fhealthcheck.jpeg)
- **/api/questions/** - post запрос, в теле которого {"questions_num": int}. Во время обработки запроса обращаемся к открытому
API https://jservice.io/api/random?count={questions_num}. Принимаем от API вопросы к викторине и ответы на них. Далее
сохраняем вопрос, ответ, дату создания в базе данных со столбцами id (int, pk), question (str, unique), answer(str),
created_at(datetime). Если в БД содержится запись с question, делаем повторные запросы в открытый API до тех пор, пока
не получим уникальный вопрос. Ответ на запрос: последний созданный при предыдущем запросе к эндпойнту вопрос. Если
объектов в БД нет, выводится пустой объект - {}
![post.jpeg](screenshots%2Fpost.jpeg)
- **/api/questions/** - get запрос с параметром question_id (int). Возвращает из БД объект с id, указанным в параметре запроса.
![get.jpeg](screenshots%2Fget.jpeg)

# Как запустить:
- в директории project создаем .env файл со следующим содержимым:
```
DATABASE_PORT=5432
POSTGRES_PASSWORD=password123
POSTGRES_USER=postgres
POSTGRES_DB=fastapi
POSTGRES_HOST=postgres
POSTGRES_HOSTNAME=127.0.0.1
```
- в корне проекта, где находится файл docker-compose.yml вводим команду
```
docker-compose up --build
```
- проверяем состояние сервиса
```
http://127.0.0.1:8000/api/healthchecker
```
- работаем с эндпойнтами API
```
http://127.0.0.1:8000/api/questions/
```
- или идем в docs
```
http://127.0.0.1:8000/docs
```




