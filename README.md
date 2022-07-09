## Автоматизация поиска сайта через google.

### Автотест 
 - 🧨 Поиск сайта ч.з google;
 - 🧨 Переход по ссылке;
 - 🧨 Сравнение контактной информации;

## Инструменты:
<p align="left"><img src="https://img.icons8.com/fluency/48/000000/python.png" alt="python" width="40" height="40"/>
<img src="https://res.cloudinary.com/batalova/image/upload/v1657359741/icons8-selenium-48_j62nbg.png" alt="selenium" width="40" height="40"/>
</p>

### Как запустить проект:


### Клонировать репозиторий: ###
```shell
git clone https://github.com/batalova90/test_site/
```
### Установить зависимости из файла requirements.txt: ###
Создать виртуальное окружение: 
```shell
python3 -m venv venv
```
Подключить виртуальное окружение:
```shell
source venv/bin/activate
```
Установить все зависимости:
```shell
python3 -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```
Запуск теста:
```shell
pytest --disable-pytest-warnings --browser=chrome (firefox)
```
- 🧨 Фикстуры и тест находятся в директории tests
