-- Примеры использования функций агрегации

--COUNT: Подсчет количества записей.
SELECT COUNT(*) AS количество_заказов FROM "Заказы";

-- SUM: Суммирование значений.
SELECT SUM("СтоимостьПродажи") FROM "Товары";

--AVG: Среднее значение.
SELECT AVG("СтоимостьПродажи") AS средняя_стоимость FROM "Товары";

--MAX: Нахождение максимального значения.
SELECT MAX("ДатаРазмещения") AS последняя_дата_размещения FROM "Заказы";

--MIN: Нахождение минимального значения.
SELECT MIN("ДатаРазмещения") AS первая_дата_размещения FROM "Заказы";

--GROUP_CONCAT: Объединение значений в одну строку (аналог в PostgreSQL — STRING_AGG).
SELECT STRING_AGG("НаименованиеТовара", ', ') AS все_товары FROM "Товары";

--COUNT с GROUP BY: Подсчет записей по группам.
SELECT "КодПоставщика", COUNT(*) AS количество_поставок
FROM "Поставка"
GROUP BY "КодПоставщика";

--SUM с GROUP BY: Суммирование значений по группам.
SELECT "НаименованиеТовара", SUM("СтоимостьПродажи") AS Метплов_продана_на_сумму
FROM "Товары"
GROUP BY "НаименованиеТовара";

--AVG с GROUP BY: Среднее значение по группам.
SELECT "НаименованиеТовара", AVG("СтоимостьПродажи") AS средняя_сумма
FROM "Товары"
GROUP BY "НаименованиеТовара";

--MAX с GROUP BY: Максимальное значение по группам.
SELECT "КодПоставщика", MAX("ДатаПоставки") AS последняя_дата
FROM "Поставка"
GROUP BY "КодПоставщика";

--MIN с GROUP BY: Минимальное значение по группам.
SELECT "КодПоставщика", MIN("ДатаПоставки") AS первая_дата
FROM "Поставка"
GROUP BY "КодПоставщика";

--COUNT DISTINCT: Подсчет уникальных значений.
SELECT COUNT(DISTINCT "КодТовара") AS уникальные_товары FROM "Заказы";

--SUM DISTINCT: Суммирование уникальных значений (если значения повторяются, учитываются только уникальные).
SELECT SUM(DISTINCT "СтоимостьПродажи") AS уникальная_сумма FROM "Товары";

--AVG DISTINCT: Среднее значение уникальных значений.
SELECT AVG(DISTINCT "СтоимостьПродажи") AS средняя_стоимость FROM "Товары";

--GROUP_CONCAT с GROUP BY: Объединение значений в одну строку по группам.
SELECT "КодПоставки", STRING_AGG("НаименованиеТовара", ', ') AS товары
FROM "Товары"
GROUP BY "КодПоставки";

--COUNT с HAVING: Подсчет записей с условием.
SELECT "КодСотрудника", COUNT(*) AS количество_заказов
FROM "Заказы"
GROUP BY "КодСотрудника"
HAVING COUNT(*) > 5;

--SUM с HAVING: Суммирование значений с условием.
SELECT "НаименованиеТовара", SUM("СтоимостьПродажи") AS общая_сумма
FROM "Товары"
GROUP BY "НаименованиеТовара"
HAVING SUM("СтоимостьПродажи") > 50000;

--AVG с HAVING: Среднее значение с условием.
SELECT "НаименованиеТовара", AVG("СтоимостьПродажи") AS средняя_сумма
FROM "Товары"
GROUP BY "НаименованиеТовара"
HAVING AVG("СтоимостьПродажи") > 50000;

--MAX с HAVING: Максимальное значение с условием.
SELECT "НаименованиеТовара", MAX("СтоимостьПродажи") AS максимальная_сумма
FROM "Товары"
GROUP BY "НаименованиеТовара"
HAVING MAX("СтоимостьПродажи") > 50000;

--MIN с HAVING: Минимальное значение с условием.
SELECT "НаименованиеТовара", MIN("СтоимостьПродажи") AS минимальная_сумма
FROM "Товары"
GROUP BY "НаименованиеТовара"
HAVING MIN("СтоимостьПродажи") < 50000;