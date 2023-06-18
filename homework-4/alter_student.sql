-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student (
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
	);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student ( first_name, last_name, birth_date, phone) VALUES ('Петров', 'Петр', '18.06.1998', '8-950-057-05-23');
INSERT INTO student ( first_name, last_name, birth_date, phone) VALUES ('Кузнецов', 'Алексей', '10.04.2000', '8-800-555-35-35');
INSERT INTO student ( first_name, last_name, birth_date, phone) VALUES ('Седых', 'Николай', '25.12.1980', '8-999-777-77-11');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;