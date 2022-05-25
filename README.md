# fe-autotests

Для локального запуска тестов необходимо

* Установить chromedriver версии, совпадающей с вашим chrome browser https://chromedriver.chromium.org/downloads
* Добавить chromedriver в PATH
* В fixtures/app.py :
`line 42 worker = "gw0"`
строку 55 - закомментировать, 57-59 - раскоментировать


`python -m venv ~/env/fe-autotests`
`source ~/env/fe-autotests/bin/activate`
`pip install -U -r requirements.txt`