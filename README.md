# Финальный проект 5-го спринта 
1. Основа для написания автотестов — фреймворк pytest + selenium.
2. Установить selenium webdriver — pip install selenium.
3. Установить pytest - pip install pytest
4. Установить плагин для определения очередности выполнения тестов (сначала должен появиться зарегистрированный пользователь, потом остальные тесты) - pip install pytest-order
5. Команда для запуска — pytest -v.

## conftest.py
Заданы основные фикстуры, которые будут использоваться в течение одной сессии тестов:
- запуск вебдрайвера, на выбор: Chrome или FireFox
- открытие стартовой страницы приложения
- заготовка для явных ожиданий до 5 секунд
- сгенерированы логин и пароль, которые будут использоваться в течение сессии

## locators.py
Модуль, в котором собраны все используемые в тестах локаторы

## test_registration_page.py
Содержит два теста регистрации: 
- Успешная регистрация
- Регистрация с некорректным паролем, получение ошибки

## test_login_page.py
Содержит четыре теста авторизации зарегистрированного пользователя:
- вход по кнопке «Войти в аккаунт» на главной,
- вход через кнопку «Личный кабинет»,
- вход через кнопку в форме регистрации,
- вход через кнопку в форме восстановления пароля.

## test_personal_area.py
Содержит четыре теста:
- Переход в личный кабинет по клику на «Личный кабинет»,
- Переход из личного кабинета в конструктор по клику на «Конструктор»,
- Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers,
- Выход из аккаунта по кнопке «Выйти» в личном кабинете.

## test_constructor_page.py
Содержит три теста:
- Переход к разделу «Булки» (этот раздел по умолчанию в начале, поэтому сначала переход к другому разделу, потом обратно),
- Переход к разделу «Соусы»,
- Переход к разделу «Начинки».
