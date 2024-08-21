INSERT INTO public."Клиент" ("Код", "ФИО", "Адрес", "Телефон") VALUES
(1, 'Иванов Иван Иванович', 'г. Москва, ул. Ленина, д. 1', '+7-900-000-0001'),
(2, 'Петров Петр Петрович', 'г. Санкт-Петербург, ул. Невский проспект, д. 10', '+7-900-000-0002'),
(3, 'Сидоров Сидор Сидорович', 'г. Новосибирск, ул. Ленина, д. 2', '+7-900-000-0003'),
(4, 'Кузнецов Алексей Алексеевич', 'г. Екатеринбург, ул. Малышева, д. 50', '+7-900-000-0004'),
(5, 'Смирнов Александр Александрович', 'г. Казань, ул. Баумана, д. 3', '+7-900-000-0005'),
(6, 'Ковалев Сергей Сергеевич', 'г. Нижний Новгород, ул. Горького, д. 15', '+7-900-000-0006'),
(7, 'Зайцев Дмитрий Дмитриевич', 'г. Самара, ул. Ленина, д. 6', '+7-900-000-0007'),
(8, 'Павлов Михаил Михайлович', 'г. Омск, ул. Советская, д. 8', '+7-900-000-0008'),
(9, 'Семенов Николай Николаевич', 'г. Челябинск, ул. Кировская, д. 9', '+7-900-000-0009'),
(10, 'Морозов Андрей Андреевич', 'г. Ростов-на-Дону, ул. Большая Садовая, д. 10', '+7-900-000-0010');


INSERT INTO public."Поставщик" ("КодПоставщика", "НазваниеПоставщика", "ПредставительПоставщика", "Обращаться", "КонтактныйТелефон", "Адрес") VALUES
(201, 'ООО Ромашка', 'Иван Иванов', 'г-н Иванов', '+7-900-000-0011', 'г. Москва, ул. Ленина, д. 11'),
(202, 'ООО Лилия', 'Петр Петров', 'г-н Петров', '+7-900-000-0012', 'г. Санкт-Петербург, ул. Ленина, д. 12'),
(203, 'ООО Василек', 'Сидор Сидоров', 'г-н Сидоров', '+7-900-000-0013', 'г. Новосибирск, ул. Ленина, д. 13'),
(204, 'ООО Роза', 'Алексей Кузнецов', 'г-н Кузнецов', '+7-900-000-0014', 'г. Екатеринбург, ул. Ленина, д. 14'),
(205, 'ООО Тюльпан', 'Александр Смирнов', 'г-н Смирнов', '+7-900-000-0015', 'г. Казань, ул. Ленина, д. 15'),
(206, 'ООО Пион', 'Сергей Ковалев', 'г-н Ковалев', '+7-900-000-0016', 'г. Нижний Новгород, ул. Ленина, д. 16'),
(207, 'ООО Лотос', 'Дмитрий Зайцев', 'г-н Зайцев', '+7-900-000-0017', 'г. Самара, ул. Ленина, д. 17'),
(208, 'ООО Лаванда', 'Михаил Павлов', 'г-н Павлов', '+7-900-000-0018', 'г. Омск, ул. Ленина, д. 18'),
(209, 'ООО Георгин', 'Николай Семенов', 'г-н Семенов', '+7-900-000-0019', 'г. Челябинск, ул. Ленина, д. 19'),
(210, 'ООО Хризантема', 'Андрей Морозов', 'г-н Морозов', '+7-900-000-0020', 'г. Ростов-на-Дону, ул. Ленина, д. 20');

INSERT INTO public."Сотрудники" ("КодСотрудника", "Фамилия", "Имя", "Отчество", "Должность", "Адрес", "ДомашнийТелефон", "ДатаРождения") VALUES
(101, 'Иванов', 'Алексей', 'Викторович', 'Менеджер', 'г. Москва, ул. Пушкина, д. 1', '+7-900-000-0101', '1985-01-01'),
(102, 'Петров', 'Денис', 'Андреевич', 'Аналитик', 'г. Санкт-Петербург, ул. Пионерская, д. 10', '+7-900-000-0102', '1986-02-02'),
(103, 'Смирнова', 'Мария', 'Владимировна', 'Программист', 'г. Новосибирск, ул. Красная, д. 2', '+7-900-000-0103', '1987-03-03'),
(104, 'Кузнецова', 'Ольга', 'Алексеевна', 'Тестировщик', 'г. Екатеринбург, ул. Малышева, д. 50', '+7-900-000-0104', '1988-04-04'),
(105, 'Смирнова', 'Екатерина', 'Александровна', 'Администратор', 'г. Казань, ул. Кремлевская, д. 3', '+7-900-000-0105', '1989-05-05'),
(106, 'Ковалев', 'Игорь', 'Павлович', 'Аналитик', 'г. Нижний Новгород, ул. Октябрьская, д. 15', '+7-900-000-0106', '1990-06-06'),
(107, 'Зайцев', 'Анатолий', 'Семенович', 'Системный администратор', 'г. Самара, ул. Ленина, д. 6', '+7-900-000-0107', '1984-07-07'),
(108, 'Павлова', 'Наталья', 'Михайловна', 'Руководитель отдела', 'г. Омск, ул. Советская, д. 8', '+7-900-000-0108', '1983-08-08'),
(109, 'Семенова', 'Юлия', 'Петровна', 'Бухгалтер', 'г. Челябинск, ул. Ленина, д. 9', '+7-900-000-0109', '1982-09-09'),
(110, 'Морозов', 'Дмитрий', 'Алексеевич', 'Финансовый директор', 'г. Ростов-на-Дону, ул. Большая Садовая, д. 10', '+7-900-000-0110', '1981-10-10');

INSERT INTO public."Поставка" ("КодПоставки", "КодПоставщика", "ДатаПоставки") VALUES
(1, 201, '2024-07-01'),
(2, 202, '2024-07-02'),
(3, 203, '2024-07-03'),
(4, 204, '2024-07-04'),
(5, 205, '2024-07-05'),
(6, 206, '2024-07-06'),
(7, 207, '2024-07-07'),
(8, 208, '2024-07-08'),
(9, 209, '2024-07-09'),
(10, 210, '2024-07-10');


INSERT INTO public."Товары" ("КодТовара", "КодПоставки", "НаименованиеТовара", "ТехническиеХарактеристики", "Описание", "Изображение", "СтоимостьЗакупки", "Наличие", "Количество", "СтоимостьПродажи") VALUES
(1001, 1, 'Неодим', 'Высокая магнитная проницаемость', 'Редкоземельный металл, используемый в производстве постоянных магнитов', NULL, '50000', 'Да', 100, 70000),
(1002, 2, 'Самарий', 'Высокая температура Кюри', 'Редкоземельный металл, используется в производстве магнитов и ядерных реакторов', NULL, '45000', 'Да', 80, 65000),
(1003, 3, 'Гадолиний', 'Большое сечение захвата нейтронов', 'Используется в ядерной энергетике и магнитно-резонансной томографии (МРТ)', NULL, '60000', 'Да', 120, 85000),
(1004, 4, 'Диспрозий', 'Высокая температура Кюри, магнитострикция', 'Применяется в производстве ядерных реакторов и магнитострикционных устройств', NULL, '70000', 'Да', 90, 95000),
(1005, 5, 'Тербий', 'Магнитострикция, люминесценция', 'Используется в производстве магнитострикционных материалов и люминофоров', NULL, '80000', 'Да', 70, 110000),
(1006, 6, 'Эрбий', 'Низкая токсичность, оптические свойства', 'Применяется в лазерах и оптических волокнах', NULL, '55000', 'Да', 60, 75000),
(1007, 7, 'Иттербий', 'Полупроводниковые свойства', 'Используется в электронике и ядерной медицине', NULL, '65000', 'Да', 110, 90000),
(1008, 8, 'Церий', 'Сильные окислительные свойства', 'Применяется в каталитических преобразователях и стекольной промышленности', NULL, '40000', 'Да', 200, 55000),
(1009, 9, 'Лантан', 'Высокая электрохимическая активность', 'Используется в производстве аккумуляторов и специальных стекол', NULL, '35000', 'Да', 150, 50000),
(1010, 10, 'Лютеций', 'Редкость, стабильность', 'Применяется в производстве сканирующих зондов и ядерных технологий', NULL, '90000', 'Да', 50, 120000);

INSERT INTO public."Заказы" ("КодЗаказа", "КодСотрудника", "КодТовара", "ДатаРазмещения", "ДатаИсполнения", "КодКлиента") VALUES
(1, 101, 1001, '2024-08-01', '2024-08-05', 1),
(2, 102, 1002, '2024-08-02', '2024-08-06', 2),
(3, 103, 1003, '2024-08-03', '2024-08-07', 3),
(4, 104, 1004, '2024-08-04', '2024-08-08', 4),
(5, 105, 1005, '2024-08-05', '2024-08-09', 5),
(6, 106, 1006, '2024-08-06', '2024-08-10', 6),
(7, 107, 1007, '2024-08-07', '2024-08-11', 7),
(8, 108, 1008, '2024-08-08', '2024-08-12', 8),
(9, 109, 1009, '2024-08-09', '2024-08-13', 9),
(10, 110, 1010, '2024-08-10', '2024-08-14', 10);
