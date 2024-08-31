SELECT *
FROM Клиент;

--  Обновление адреса клиента:
UPDATE Клиент
SET "Адрес" = 'г. Москва, ул. Злачная, д. 1'
WHERE "Код" = 1;

-- Изменение должности сотрудника:
UPDATE Сотрудники
SET "Должность" = 'Data аналитик'
WHERE "КодСотрудника" = 102;

UPDATE Сотрудники
SET "Должность" = 'Главный Пиздабол'
WHERE "Фамилия" = 'Морозов' and "Имя" = 'Дмитрий' and "Отчество" = 'Алексеевич';

-- Обновление наименования товара
UPDATE public."Товары"
SET "НаименованиеТовара" = 'Гадолиний высокой чистоты'
WHERE "КодТовара" = 1003;

-- Изменение даты размещения заказа:
UPDATE Заказы
SET "ДатаРазмещения" = '2024-08-10'
WHERE "КодЗаказа" = 4;

-- Обновление контактного телефона поставщика:
UPDATE Поставщик
SET "КонтактныйТелефон" = '+7-900-505-0099'
WHERE "КодПоставщика" = 205;

-- Изменение даты исполнения заказа:
UPDATE Заказы
SET "ДатаИсполнения" = '2024-08-15'
WHERE "КодЗаказа" = 2;

-- Обновление имени сотрудника:
UPDATE Сотрудники
SET "Имя" = 'Николай'
WHERE "КодСотрудника" = 103;

-- Изменение стоимости товара:
UPDATE Товары
SET "СтоимостьПродажи" = 150000
WHERE "КодТовара" = 1004;

-- Обновление представителя поставщика:
UPDATE Поставщик
SET "ПредставительПоставщика" = 'Ольга Иванова'
WHERE "КодПоставщика" = 203;

-- Изменение домашнего телефона сотрудника:
UPDATE Сотрудники
SET "ДомашнийТелефон" = '+7-900-000-0111'
WHERE "КодСотрудника" = 104;

-- Обновление наименования клиента:
UPDATE Клиент
SET "ФИО" = 'Чудак На М'
WHERE "Код" = 6;

-- Изменение даты поставки:
UPDATE Поставка
SET "ДатаПоставки" = '2024-07-15'
WHERE "КодПоставки" = 3;

-- Обновление описания товара:
UPDATE Товары
SET "Описание" = 'Иттрий высокой чистоты, применяемый в высокотехнологичных устройствах'
WHERE "КодТовара" = 1002;

-- Изменение адреса сотрудника:
UPDATE Сотрудники
SET "Адрес" = 'г. Санкт-Петербург, ул. Невский проспект, д. 100'
WHERE "КодСотрудника" = 105;

-- Обновление имени клиента:
UPDATE Клиент
SET "ФИО" = 'Сергеев Сергей Сергеевич'
WHERE "Код" = 7;

-- Изменение наличия товара:
UPDATE Товары
SET "Наличие" = 'Нет'
WHERE "КодТовара" = 1005;

-- Обновление должности сотрудника:
UPDATE public."Сотрудники"
SET "Должность" = 'Руководитель отдела продаж'
WHERE "КодСотрудника" = 106;

-- Изменение даты исполнения заказа:
UPDATE Заказы
SET "ДатаИсполнения" = '2024-08-20'
WHERE "КодЗаказа" = 7;

-- Обновление контактного телефона клиента:
UPDATE Клиент
SET "Телефон" = '+7-777-000-0021'
WHERE "Код" = 9;

-- Изменение стоимости закупки товара:
UPDATE Товары
SET "СтоимостьЗакупки" = '120000'
WHERE "КодТовара" = 1006;