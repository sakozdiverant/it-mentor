-- Создайте view любой таблицы
-- Когда кто кому что продал
CREATE VIEW заказ_информация AS
SELECT
    z."КодЗаказа",
    z."ДатаРазмещения",
    z."ДатаИсполнения",
    s."Фамилия" || ' ' || s."Имя" || ' ' || COALESCE(s."Отчество", '') AS "ФИО_сотрудника",
    c."ФИО" AS "ФИО_клиента",
    t."НаименованиеТовара"
FROM
    "Заказы" z
JOIN
    "Сотрудники" s ON z."КодСотрудника" = s."КодСотрудника"
JOIN
    "Клиенты" c ON z."КодКлиента" = c."Код"
JOIN
    "Товары" t ON z."КодТовара" = t."КодТовара";


-- Уникальный список городов
CREATE VIEW Город AS
SELECT DISTINCT
    REPLACE(SUBSTRING("Адрес" FROM 1 FOR POSITION(',' IN "Адрес") - 1), 'г. ', '') AS "Город"
SELECT DISTINCT "Город"
FROM "Клиенты";

