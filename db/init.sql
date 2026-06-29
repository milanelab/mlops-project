CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    age INT,
    pressure INT,
    cholesterol INT
);

INSERT INTO data (age, pressure, cholesterol) VALUES
(20, 120, 200),
(30, 130, 220),
(40, 140, 240);