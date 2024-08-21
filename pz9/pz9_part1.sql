CREATE TABLE public."Клиент" (
    "Код" INTEGER PRIMARY KEY NOT NULL,
    "ФИО" VARCHAR(255) NOT NULL,
    "Адрес" TEXT NOT NULL,
    "Телефон" VARCHAR(15) NOT NULL
);


CREATE TABLE public."Поставщик" (
    "КодПоставщика" INTEGER PRIMARY KEY NOT NULL,
    "НазваниеПоставщика" VARCHAR(100) NOT NULL,
    "ПредставительПоставщика" VARCHAR(100),
    "Обращаться" VARCHAR(100) NOT NULL,
    "КонтактныйТелефон" VARCHAR(100) NOT NULL,
    "Адрес" TEXT
);

CREATE TABLE public."Поставка" (
    "КодПоставки" INTEGER PRIMARY KEY NOT NULL,
    "КодПоставщика" INTEGER NOT NULL,
    "ДатаПоставки" DATE,
    FOREIGN KEY ("КодПоставщика") REFERENCES public."Поставщик" ("КодПоставщика")
);


CREATE TABLE public."Сотрудники" (
    "КодСотрудника" INTEGER PRIMARY KEY NOT NULL,
    "Фамилия" VARCHAR(100) NOT NULL,
    "Имя" VARCHAR(100) NOT NULL,
    "Отчество" VARCHAR(100),
    "Должность" VARCHAR(100) NOT NULL,
    "Адрес" TEXT,
    "ДомашнийТелефон" VARCHAR(15),
    "ДатаРождения" DATE
);


CREATE TABLE public."Товары" (
    "КодТовара" INTEGER PRIMARY KEY NOT NULL,
    "КодПоставки" INTEGER NOT NULL,
    "НаименованиеТовара" VARCHAR(100) NOT NULL,
    "ТехническиеХарактеристики" VARCHAR(100) NOT NULL,
    "Описание" VARCHAR(100) NOT NULL,
    "Изображение" TEXT,
    "СтоимостьЗакупки" VARCHAR(15) NOT NULL,
    "Наличие" VARCHAR(3) NOT NULL,
    "Количество" INTEGER NOT NULL,
    "СтоимостьПродажи" INTEGER NOT NULL,
    FOREIGN KEY ("КодПоставки") REFERENCES public."Поставка" ("КодПоставки")
);


CREATE TABLE public."Заказы" (
    "КодЗаказа" INTEGER PRIMARY KEY NOT NULL,
    "КодСотрудника" INTEGER NOT NULL,
    "КодТовара" INTEGER NOT NULL,
    "ДатаРазмещения" DATE NOT NULL,
    "ДатаИсполнения" DATE,
    "КодКлиента" INTEGER NOT NULL,
    FOREIGN KEY ("КодСотрудника") REFERENCES public."Сотрудники" ("КодСотрудника"),
    FOREIGN KEY ("КодТовара") REFERENCES public."Товары" ("КодТовара"),
    FOREIGN KEY ("КодКлиента") REFERENCES public."Клиент" ("Код")
);
