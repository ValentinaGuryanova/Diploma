## Diploma  Сервис покупки товаров для авторизованных пользователей

# Задача

Разработать API backend на Python Сервис покупки товаров для авторизованных пользователей. В качестве БД использовать MySQL или PostgreSQL. 

PostgreSQL
ORM
FastAPI
Tortoise
Git
Readme
PEP8
Swagger

# План работы:

1. Создать в PyCharm FastAPI_project и внести необходимые настройки, установить зависимости, виртуальное окружение.
2. Создать базу данных в PostgreSQL.
3. Создать модель User с полями (ФИО, email, телефон, пароль, подтверждение пароля).
4. Создать модель Product с полями (наименование, стоимость, дата создания, дата изменения, признак актуальности).
5. Описать необходимые роутеры.
6. Реализовать функцию по созданию суперпользователя и групп пользователей.
7. Наполнить базу данных.
8. Реализовать функционал по регистрации и авторизации для неавторизованных пользователей.
9. Реализовать функционал верификации пользователя через почту либо телефон.
10. Реализовать функционал вывода пагинированных товаров для авторизованных пользователей.
11. Написать функцию по созданию пароля.
12. Написать функцию по созданию маски для номера телефона.
13. Написать тесты и протестировать.
14. Проверить на соответствие pep8.
15. Разместить на GitHub.

**Требуемый функционал**
1. Регистрация: ФИО, email (уникальный), телефон (уникальный), пароль, подтверждение пароля.
Все поля обязательны.

2. Пароль должен быть не менее 8 символов, только латиница, минимум 1 символ верхнего регистра, минимум 1 спец символ $%&!:. Телефон должен удовлетворять маске: начинаться с +7 после чего идет 10 цифр.

3. Авторизация: email или телефон (одно поле), пароль
Для авторизованных пользователей доступна таблица товаров, где выводится список всех активных товаров в базе данных

4.Товар: name(str), price(int), created_at(datetime), updated_at(datetime), is_active(bool)

Доп задача:
Должен быть реализован объект Корзина (list[Товар]), в котором можно через getter получить общую стоимость корзины, реализовать методы добавления (одного или нескольких, используя @overload), удаления товара\полную очистку
Вывод корзины и работу с ней реализовывать не обязательно, достаточно только класса

**Методы доступные неавторизованным пользователям**: регистрация, авторизация
При попытке получить данные без доступа выводить ошибку {code: 401, message:”Unauthorized”}, с HTTP statuscode 401

**Методы доступные авторизованным пользователям**: список пагинированных товаров

Желательно использовать асинхронность

# Требуемый стэк

- python
- postgresql

# Условия приемки

- код размещен в открытом репозитории
- код покрыт тестами минимум на 75%
- код оформлен согласно pep8
- оформлен Readme файл

Идентификация пользователя должна происходить по Bearer токену или JWT.
