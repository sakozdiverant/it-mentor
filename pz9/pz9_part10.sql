--Добавьте поле "Общая сумма" в Товары
ALTER TABLE "Товары"
ADD COLUMN "ОбщаяСумма" numeric(15, 2);

-- создаем функцию update_total_value()
-- Обновляем поле "ОбщаяСумма" на основе "СтоимостьПродажи" и "Количество"
CREATE OR REPLACE FUNCTION update_total_value()
RETURNS TRIGGER AS $$
BEGIN
    NEW."ОбщаяСумма" := NEW."СтоимостьПродажи" * NEW."Количество";
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--Создайте триггер:
CREATE TRIGGER trg_update_total_value
BEFORE UPDATE ON "Товары"
FOR EACH ROW
EXECUTE FUNCTION update_total_value();

--Test
INSERT INTO "Товары" ("КодТовара", "КодПоставки", "НаименованиеТовара", "ТехническиеХарактеристики", "Описание", "Изображение", "СтоимостьЗакупки", "Наличие", "Количество", "СтоимостьПродажи")
VALUES (1001, 1, 'Фалаиметатор', 'Пластик', 'Sex игрушка', 'А вам есть 18?', '100.00', 'да', 10, 200.00);
UPDATE "Товары"
SET "Количество" = 15
WHERE "КодТовара" = 1001;
SELECT *
FROM Товары;
