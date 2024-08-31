-- Настриваем каскадное удаление для будущих записей
-- Удалите старое ограничение внешнего ключа
ALTER TABLE "Заказы"
DROP CONSTRAINT "Заказы_КодКлиента_fkey";

-- Удаление всех строк из таблицы Клиенты, где Телефон  с '2222222222':
DELETE FROM "Клиенты"
WHERE "Телефон" = '2222222222';

--Удаление строки из таблицы Поставка с определенным КодПоставки:
ALTER TABLE "Товары"
DROP CONSTRAINT "Товары_КодПоставки_fkey";
DELETE FROM "Поставка"
WHERE "КодПоставки" = 10;

--Удаление всех строк из таблицы Заказы:
DELETE FROM "Заказы";

--Удаление всех строк из таблицы Товары:
TRUNCATE TABLE "Товары" CASCADE;

--Очистить таблицу Клиенты и все связанные таблицы:
TRUNCATE TABLE "Клиенты" CASCADE;