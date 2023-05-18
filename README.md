# Rostelekom.

Для запуска тестов необходимо выполнить команду: python3 -m pytest -s -v --driver Chrome --driver-path /home/agata/.local/bin/chromedriver test_redirect.py -k 'test_название_теста'

/test_redirect.py - Файл содержит ряд тестов для страниц авторизации Ростелекома (https://b2c.passport.rt.ru/)
для выполнения теста test_password_change, требуется ввод капчи в строку терминала

/conftest.py содержит некоторые вспомогательные элементы 

/pages.py  содержит реализацию шаблона PageObject для Python
