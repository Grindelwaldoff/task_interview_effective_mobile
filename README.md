# task_interview_effective_mobile


## Описание:
Реализация тестового задания для компании Effective Mobile.

## ТЗ:
#### Функционал:
* Вывод постранично записей из справочника на экран
* Добавление новой записи в справочник
* Возможность редактирования записей в справочнике
* Поиск записей по одной или нескольким характеристикам
#### Требования к программе:
* Реализация интерфейса через консоль (без веб- или графического интерфейса)
* Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
* В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

## Гайд:
Код принимает все команды пока не будет введена команда:
```
exit
```
Поддерживаемые команды и формат ввода данных:
Отображение всех добвленных в справочник контактов:
```
get_contact
```
Добавление новых данных в справочник:
```
add_contact name=value surname=value middle_name=value company=value privat_phone=value work_phone=value
```
Изменение существующих данных (важно указать id, тк как все данные индексируются и поиск осуществялется именно по этому пораметру. Дальше указывается необходимый параметр и его значение, как при добавлении.):
```
edit_contact id=value param=value
```
Поиск записи по нескольким или одному значениям (поиск выдаст результат, только если оба значения удалось найти в элемете справочника):
```
find_contact vsevolod rybnik
```

## Структура бд:
Бд представляет из себя текстовый файл с данными в следующем порядке (что также указано в 1 строчке файла):
* id | surname | name | company | privat_phone | work_phone

## Время за которое был разработан данный алгоритм:
4 часа

## Разработчик:
Всеволод Рыбник tg: @Grindelwaldoff
