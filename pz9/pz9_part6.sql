-- Индекс для таблицы "Клиенты" по колонке "ФИО"
CREATE INDEX idx_клиенты_фио ON "Клиенты" ("ФИО");

-- Индекс для таблицы "Поставщик" по колонке "НазваниеПоставщика"
CREATE INDEX idx_поставщик_название ON "Поставщик" ("НазваниеПоставщика");

-- Индекс для таблицы "Сотрудники" по колонке "Фамилия"
CREATE INDEX idx_сотрудники_фамилия ON "Сотрудники" ("Фамилия");

-- Индекс для таблицы "Товары" по колонке "НаименованиеТовара"
CREATE INDEX idx_товары_наименование ON "Товары" ("НаименованиеТовара");

-- Индекс для таблицы "Заказы" по колонке "КодКлиента"
CREATE INDEX idx_заказы_код_клиента ON "Заказы" ("КодКлиента");

-- Индекс для таблицы "Поставка" по колонке "ДатаПоставки"
CREATE INDEX idx_поставка_дата ON "Поставка" ("ДатаПоставки");

-- Индекс для таблицы "Товары" по колонке "КодПоставки"
CREATE INDEX idx_товары_код_поставки ON "Товары" ("КодПоставки");

-- Индекс для таблицы "Заказы" по колонке "КодТовара"
CREATE INDEX idx_заказы_код_товара ON "Заказы" ("КодТовара");

-- Индекс для таблицы "Поставщик" по колонке "КонтактныйТелефон"
CREATE INDEX idx_поставщик_телефон ON "Поставщик" ("КонтактныйТелефон");

-- Индекс для таблицы "Сотрудники" по колонке "Должность"
CREATE INDEX idx_сотрудники_должность ON "Сотрудники" ("Должность");