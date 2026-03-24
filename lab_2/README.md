# Лабораторная работа 2: Микросервисная REST API система

## Вариант

**Вариант 10: Планирование задач**

## Реализованные сервисы

- `proxy_service` - единая точка входа
- `auth_service` - JWT аутентификация
- `user_service` - пользователи (исполнители)
- `goal_service` - цели
- `task_service` - задачи
- `notification_service` - mock сервис (TODO для расширения)
- `calendar_service` - mock сервис (TODO для расширения)

## Хранилище

Все сервисы используют in-memory хранилище в рамках контейнера.

## Запуск

```bash
cd lab_2
docker compose up --build
```

Прокси доступен на `http://localhost:8000`.
Swagger прокси: `http://localhost:8000/docs`.

## Основные endpoint'ы через proxy

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/users`
- `GET /api/v1/users/by-login/{login}`
- `GET /api/v1/users/search?mask=...`
- `POST /api/v1/goals`
- `GET /api/v1/goals`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks/by-goal/{goal_id}`
- `PATCH /api/v1/tasks/{task_id}/status`

## Тесты

```bash
cd lab_2
pytest --cov=backend --cov-report=term-missing --cov-report=xml
```
