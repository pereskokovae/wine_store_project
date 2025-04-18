# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите и активируйте виртуальное окружение командами:
```
python3 -m venv venv\
```
```
venv\Scripts\activate
```

- Скачайте все зависимости используя команду:
```
pip install -r requirements.txt
```

- Запустите сайт командой:
```
python3 main.py
```

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Входные даные которые можно менять

Вы можете редактировать каталог вина на сайте используя табличку Exel. 

- Откройте [Exel файл](https://dvmn.org/filer/canonical/1610450335/764/), внутри вы увидете табличку которая будет выглядеть примерно вот так.

|Категория|Название|Сорт|Цена|Картинка|Акция|
|Запись в столбце 1|Запись в столбце 2|Запись в столбце 3|Запись в столбце 4|Запись в столбце 5|Запись в столбце 6|
|Запись в столбце 1|Запись в столбце 2|Запись в столбце 3|Запись в столбце 4|Запись в столбце 5|Запись в столбце 6|


- Чтобы добавить новую карточку, вам необходимо начать писать с новой строки.

1. В первой колонке напишите категорию продукта, можете использовать те же, что были выше, или использовать свою.
2. Напишите название товара.
3. Напишите сорт при его наличиии, если сорта нет-оставьте окошко пустым.
4. Напишите цену, которую хотите получить за товар.
5. Вам необходимо добавить картинку в папку `assets`. Напишите название картинки, какого еще нет, и сделайте в формате `.jpg`, после этого напишите полное название (с .jpg на конце) в пятую колонку.
6. При желании сделать акцию на товар, напишите `Выгодное предложение` в последнее окошко.



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
