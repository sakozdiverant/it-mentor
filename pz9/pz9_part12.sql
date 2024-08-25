--Создайте базу данных MongoDB

use ITM

--оздайте коллекцию для хранения документов по категориям
db.createCollection("Books")
db.createCollection("Movies")
db.createCollection("Music")

--Добавим данные
db.Books.insertMany([
                        {
                            title: "Преступление и наказание",
                            author: "Фёдор Достоевский",
                            category: "Роман",
                            year: 1866
                        },
                        {
                            title: "Мастер и Маргарита",
                            author: "Михаил Булгаков",
                            category: "Роман",
                            year: 1966
                        },
                        {
                            title: "Война и мир",
                            author: "Лев Толстой",
                            category: "Роман",
                            year: 1869
                        },
                        {
                            title: "Анна Каренина",
                            author: "Лев Толстой",
                            category: "Роман",
                            year: 1877
                        },
                        {
                            title: "Доктор Живаго",
                            author: "Борис Пастернак",
                            category: "Роман",
                            year: 1957
                        }
                    ])

db.Movies.insertMany([
                        {
                            title: "Броненосец Потёмкин",
                            director: "Сергей Эйзенштейн",
                            category: "Исторический",
                            year: 1925
                        },
                        {
                            title: "Москва слезам не верит",
                            director: "Владимир Меньшов",
                            category: "Драма",
                            year: 1979
                        },
                        {
                            title: "Иван Васильевич меняет профессию",
                            director: "Леонид Гайдай",
                            category: "Комедия",
                            year: 1973
                        },
                        {
                            title: "Андрей Рублёв",
                            director: "Андрей Тарковский",
                            category: "Исторический",
                            year: 1966
                        },
                        {
                            title: "Брат",
                            director: "Алексей Балабанов",
                            category: "Драма",
                            year: 1997
                        }
                    ])

db.Music.insertMany([
                        {
                            title: "Кукушка",
                            artist: "Виктор Цой",
                            category: "Рок",
                            year: 1990
                        },
                        {
                            title: "Я свободен",
                            artist: "Ария",
                            category: "Рок",
                            year: 2001
                        },
                        {
                            title: "Белый снег",
                            artist: "Юрий Антонов",
                            category: "Поп",
                            year: 1979
                        },
                        {
                            title: "Люди встречаются",
                            artist: "Весёлые ребята",
                            category: "Поп",
                            year: 1976
                        },
                        {
                            title: "Владимирский централ",
                            artist: "Михаил Круг",
                            category: "Шансон",
                            year: 1998
                        }
                    ])
-- Проверка данных
db.Books.find()
db.Movies.find()
db.Music.find()

--добавить индексы
db.Books.createIndex({ title: 1 })
db.Movies.createIndex({ director: 1 })
db.Music.createIndex({ artist: 1 })
