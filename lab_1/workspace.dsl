workspace "Task Planning System" "Система планирования задач для управления целями и задачами пользователей" {

    !identifiers hierarchical

    model {
        # Пользователи системы
        user = person "Пользователь" "Пользователь системы, который создает цели и управляет задачами" {
            tags "User"
        }

        # Внешние системы
        emailSystem = softwareSystem "Email Service" "Внешний сервис для отправки уведомлений по электронной почте" {
            tags "External"
        }

        ssoAuthSystem = softwareSystem "SSO Authentication Services" "Внешние сервисы аутентификации через Single Sign-On (Google, Microsoft и др.)" {
            tags "External"
        }

        # Основная система
        taskPlanningSystem = softwareSystem "Task Planning System" "Система планирования задач, позволяющая пользователям создавать цели и управлять задачами для их достижения" {
            tags "Internal"

            # Веб-сервер и прокси
            nginx = container "Nginx" "Веб-сервер, обратный прокси и балансировщик нагрузки для маршрутизации запросов, статического контента и распределения нагрузки между инстансами сервисов" "Nginx" {
                tags "WebServer"
            }

            # Веб-приложение
            webApp = container "Web Application" "Веб-интерфейс для взаимодействия пользователей с системой" "React" {
                tags "WebApplication"
            }

            # Прокси-сервис (единая точка входа)
            proxyService = container "Proxy Service" "Слой изоляции и единая точка входа для всех API запросов. Обрабатывает запросы, маршрутизирует к соответствующим сервисам, не имеет прямого доступа к БД" "Python/FastAPI" {
                tags "API"
            }

            # Сервис управления пользователями
            userService = container "User Service" "Сервис управления персональными данными пользователей: регистрация, профиль, поиск" "Python" {
                tags "Service"
            }

            # Сервис авторизации и аутентификации
            authService = container "Auth Service" "Сервис авторизации: JWT токены, аутентификация через логин/пароль и SSO" "Python" {
                tags "Service"
            }

            # Сервис уведомлений
            notificationService = container "Notification Service" "Сервис управления уведомлениями с поддержкой различных менеджеров (email, push, SMS)" "Python" {
                tags "Service"
            }

            # Сервис календарей
            calendarService = container "Calendar Service" "Сервис управления календарями и шарингом календарей между пользователями" "Python" {
                tags "Service"
            }

            # Сервис управления целями
            goalService = container "Goal Service" "Сервис для управления целями пользователей: создание, получение списка целей" "Python" {
                tags "Service"
            }

            # Сервис управления задачами
            taskService = container "Task Service" "Сервис для управления задачами: создание задач, изменение статуса, получение задач цели" "Python" {
                tags "Service"
            }

            # Брокер сообщений
            rabbitMQ = container "RabbitMQ" "Брокер сообщений для асинхронной обработки уведомлений и событий системы" "RabbitMQ" {
                tags "MessageBroker"
            }

            # Кеш
            redis = container "Redis" "Кеш для хранения сессий, токенов и часто запрашиваемых данных" "Redis" {
                tags "Cache"
            }

            # База данных
            database = container "PostgreSQL Database" "База данных для хранения информации о пользователях, целях, задачах и календарях" "PostgreSQL" {
                tags "Database"
            }

            # Мониторинг
            prometheus = container "Prometheus" "Система мониторинга и сбора метрик производительности системы" "Prometheus" {
                tags "Monitoring"
            }

            grafana = container "Grafana" "Система визуализации метрик и дашбордов для мониторинга" "Grafana" {
                tags "Monitoring"
            }
        }

        # Взаимодействия пользователя с системой
        user -> taskPlanningSystem "Обращается к системе через веб-интерфейс и API" "HTTPS"
        user -> taskPlanningSystem.nginx "Обращается к веб-интерфейсу через Nginx" "HTTPS"

        # Взаимодействия между контейнерами внутри системы
        taskPlanningSystem.nginx -> taskPlanningSystem.webApp "Отдает статический контент" "HTTP"
        taskPlanningSystem.nginx -> taskPlanningSystem.proxyService "Проксирует API запросы" "HTTPS/REST"
        taskPlanningSystem.webApp -> taskPlanningSystem.proxyService "Отправляет API запросы" "HTTPS/REST"
        taskPlanningSystem.webApp -> taskPlanningSystem.calendarService "Подключение для шаринга календарей" "WebSocket"

        # Прокси-сервис взаимодействует с другими сервисами
        taskPlanningSystem.proxyService -> taskPlanningSystem.authService "Проверка аутентификации и авторизации" "HTTP"
        taskPlanningSystem.proxyService -> taskPlanningSystem.userService "Управление пользователями" "HTTP"
        taskPlanningSystem.proxyService -> taskPlanningSystem.goalService "Управление целями" "HTTP"
        taskPlanningSystem.proxyService -> taskPlanningSystem.taskService "Управление задачами" "HTTP"
        taskPlanningSystem.proxyService -> taskPlanningSystem.calendarService "Управление календарями" "HTTP"
        taskPlanningSystem.proxyService -> taskPlanningSystem.redis "Проверка кеша" "Redis Protocol"

        # Сервисы взаимодействуют с базой данных
        taskPlanningSystem.userService -> taskPlanningSystem.database "Читает и записывает данные пользователей" "JDBC"
        taskPlanningSystem.goalService -> taskPlanningSystem.database "Читает и записывает данные целей" "JDBC"
        taskPlanningSystem.taskService -> taskPlanningSystem.database "Читает и записывает данные задач" "JDBC"
        taskPlanningSystem.calendarService -> taskPlanningSystem.database "Читает и записывает данные календарей" "JDBC"

        # Сервисы используют кеш
        taskPlanningSystem.authService -> taskPlanningSystem.redis "Хранение JWT токенов и сессий" "Redis Protocol"
        taskPlanningSystem.userService -> taskPlanningSystem.redis "Кеширование данных пользователей" "Redis Protocol"
        taskPlanningSystem.goalService -> taskPlanningSystem.redis "Кеширование списков целей" "Redis Protocol"
        taskPlanningSystem.taskService -> taskPlanningSystem.redis "Кеширование задач" "Redis Protocol"

        # Аутентификация
        taskPlanningSystem.authService -> ssoAuthSystem "Аутентификация через SSO" "OAuth2/OpenID Connect"
        taskPlanningSystem.authService -> taskPlanningSystem.database "Хранение учетных данных" "JDBC"

        # Уведомления через RabbitMQ
        taskPlanningSystem.taskService -> taskPlanningSystem.rabbitMQ "Публикует события о создании/изменении задач" "AMQP"
        taskPlanningSystem.goalService -> taskPlanningSystem.rabbitMQ "Публикует события о создании целей" "AMQP"
        taskPlanningSystem.calendarService -> taskPlanningSystem.rabbitMQ "Публикует события о календарных событиях" "AMQP"
        taskPlanningSystem.rabbitMQ -> taskPlanningSystem.notificationService "Доставляет события для обработки" "AMQP"
        taskPlanningSystem.notificationService -> emailSystem "Отправляет уведомления по email" "SMTP"

        # Мониторинг
        taskPlanningSystem.prometheus -> taskPlanningSystem.proxyService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.userService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.goalService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.taskService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.calendarService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.notificationService "Собирает метрики" "HTTP"
        taskPlanningSystem.prometheus -> taskPlanningSystem.authService "Собирает метрики" "HTTP"
        taskPlanningSystem.grafana -> taskPlanningSystem.prometheus "Запрашивает метрики для визуализации" "HTTP"
    }

    views {
        # Диаграмма System Context (C1)
        systemContext taskPlanningSystem "SystemContext" {
            include *
            autolayout lr
            title "System Context - Система планирования задач"
            description "Диаграмма контекста системы, показывающая взаимодействие пользователей и внешних систем с системой планирования задач"
        }

        # Диаграмма Container (C2)
        container taskPlanningSystem "Container" {
            include *
            title "Container - Архитектура контейнеров системы планирования задач"
            description "Диаграмма контейнеров, показывающая внутреннюю структуру системы и взаимодействие между компонентами"
        }

        # Диаграмма Dynamic для сценария создания задачи
        dynamic taskPlanningSystem "CreateTaskDynamic" "Сценарий создания новой задачи на пути к цели" {
            user -> taskPlanningSystem.nginx "Отправляет запрос через веб-интерфейс"
            taskPlanningSystem.nginx -> taskPlanningSystem.proxyService "Проксирует запрос"
            taskPlanningSystem.proxyService -> taskPlanningSystem.authService "Проверяет аутентификацию"
            taskPlanningSystem.authService -> taskPlanningSystem.redis "Проверяет JWT токен в кеше"
            taskPlanningSystem.redis -> taskPlanningSystem.authService "Возвращает результат проверки"
            taskPlanningSystem.authService -> taskPlanningSystem.proxyService "Подтверждение аутентификации"
            taskPlanningSystem.proxyService -> taskPlanningSystem.taskService "Создать задачу"
            taskPlanningSystem.taskService -> taskPlanningSystem.database "Сохранить задачу в БД"
            taskPlanningSystem.database -> taskPlanningSystem.taskService "Подтверждение сохранения с данными задачи"
            taskPlanningSystem.taskService -> taskPlanningSystem.redis "Инвалидировать старый кеш задач и сохранить новую задачу в кеш"
            taskPlanningSystem.redis -> taskPlanningSystem.taskService "Подтверждение обновления кеша"
            taskPlanningSystem.taskService -> taskPlanningSystem.rabbitMQ "Публикует событие создания задачи"
            taskPlanningSystem.rabbitMQ -> taskPlanningSystem.notificationService "Доставляет событие"
            taskPlanningSystem.notificationService -> emailSystem "Отправляет уведомление по email"
            taskPlanningSystem.taskService -> taskPlanningSystem.proxyService "Возврат созданной задачи"
            taskPlanningSystem.proxyService -> taskPlanningSystem.nginx "Возврат результата"
            taskPlanningSystem.nginx -> user "Отображение созданной задачи"
            title "Dynamic - Создание новой задачи"
            description "Последовательность взаимодействия компонентов при создании новой задачи на пути к цели"
        }

        styles {
            element "Person" {
                shape person
                color #08427b
            }
            element "User" {
                color #08427b
            }
            element "Internal" {
                background #1168bd
                color #ffffff
            }
            element "External" {
                background #999999
                color #ffffff
            }
            element "WebServer" {
                background #438dd5
                color #ffffff
            }
            element "WebApplication" {
                background #438dd5
                color #ffffff
            }
            element "API" {
                background #85bbf0
                color #000000
            }
            element "Service" {
                background #85bbf0
                color #000000
            }
            element "Database" {
                shape cylinder
                background #438dd5
                color #ffffff
            }
            element "Cache" {
                background #ff9900
                color #000000
            }
            element "MessageBroker" {
                background #ff6600
                color #ffffff
            }
            element "Monitoring" {
                background #00cc00
                color #000000
            }
            relationship "Relationship" {
                routing direct
            }
        }
    }

    configuration {
        scope softwaresystem
    }

}
