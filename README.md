# Обрезка ссылок с помощью Битли

Скрипт формирует сокращенную ссылку на указанный адрес. Если указать ранее сокращенную ссылку, то будет показано количество переходов по данной сокращенной ссылке

Для вызова программы необходимо запустить скрипт с первым параметром в виде ссылки для сокращения. 
Например:
```
python main.py https://yandex.ru
```

### Как установить

Для получения API ключа, необходимо
1. Зарегестрироваться на сервисе [bit.ly](https://bit.ly/)
2. В профиле войти в раздел Settings -> Developer settings -> API
3. В поле Access token указать свой текущий пароль

После этого появится ваш API ключ вида `bc4f0a6afas8c9eda2f2a439273b1e172b4060c1`
Данный ключ необходимо добавить в файл `.env` в каталоге с программой указав значение для переменной `BITLY_TOKEN=`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).